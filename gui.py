import customtkinter as ctk
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageGrab
# from tensorflow.keras.models import load_model

# Load the CNN model
# model = load_model('models/cnn_model.h5')
print('Model Loaded')


class DigitRecognitionApp:
    def __init__(self, root):
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme("green")
        ctk.CTkFont(family="Arial", size=14, weight="bold")

        self.root = root
        self.root.title("Digit Recognition App")

        # Set initial window size and make it resizable
        self.root.geometry("800x600")
        self.root.rowconfigure(0, weight=1, uniform="a")
        self.root.columnconfigure(0, weight=7, uniform="a")  # Left column (70%)
        self.root.columnconfigure(1, weight=3, uniform="a")  # Right column (30%)

        # Frames for layout
        self.frame_left = ctk.CTkFrame(self.root)
        self.frame_left.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")

        self.frame_right = ctk.CTkFrame(self.root,fg_color='transparent')
        self.frame_right.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="nsew")

        # Left Column: Canvas for Drawing
        self.frame_left.rowconfigure(0, weight=1)
        self.frame_left.columnconfigure(0, weight=1)

        self.canvas = Canvas(
            self.frame_left,
            bg="white",
            highlightthickness=2,  # Border thickness
            highlightbackground="gray"  # Black border around the canvas
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.canvas.bind("<Button-1>", self.activate_event)

        self.lastx, self.lasty = None, None
        self.image_number = 0

        # Right Column: Output and Buttons
        self.frame_right.rowconfigure(0, weight=1)
        self.frame_right.rowconfigure(1, weight=0)
        self.frame_right.rowconfigure(2, weight=0)
        self.frame_right.columnconfigure(0, weight=1)

        # Output Section (Top of the Right Column)
        self.output_frame = ctk.CTkFrame(self.frame_right, fg_color='#D3D3D3')
        self.output_frame.grid(row=0, column=0, pady=(0, 2), sticky="nsew")

        self.prediction_label = ctk.CTkLabel(
            self.output_frame,
            text="Predictions will be shown here",
            font=("Arial", 16, "italic"),
            anchor="center",
            wraplength=240,
            text_color="black"
        )
        self.prediction_label.grid(row=0, column=0, padx=2, pady=10, sticky="nsew")

        # Buttons (Bottom of the Right Column)
        self.btn_predict = ctk.CTkButton(
            self.frame_right,
            text="Predict",
            command=self.recognize_digit,
            width=5,
            height=40,
            corner_radius=20,
            fg_color="#FFC0CB",  # Your original pink theme
            hover_color="#FFB6C1",  # Lighter pink for hover
            text_color="black",  # Black text for readability
            font=("Arial", 14, "bold"),
        )
        self.btn_predict.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.btn_clear = ctk.CTkButton(
            self.frame_right,
            text="Clear Canvas",
            command=self.clear_canvas,
            width=5,
            height=40,
            corner_radius=20,
            fg_color="black",  # Your original black theme
            hover_color="#333333",  # Darker black/gray for hover
            text_color="white",  # White text for contrast
            font=("Arial", 14, "bold"),
        )
        self.btn_clear.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        # Bind resize event to dynamically adjust the canvas
        self.root.bind("<Configure>", self.resize_canvas)

    def resize_canvas(self, event):
        # Dynamically resize the canvas to fit the left frame
        self.canvas.config(width=self.frame_left.winfo_width(), height=self.frame_left.winfo_height())

    def draw_lines(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(
            (self.lastx, self.lasty, x, y),
            width=30, fill="black", capstyle=ROUND, smooth=TRUE, splinesteps=12
        )
        self.lastx, self.lasty = x, y

    def activate_event(self, event):
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.lastx, self.lasty = event.x, event.y

    def get_canvas_image(self, filename):
        from PIL import Image, ImageTk
        img = Image.open(filename)
        img = img.resize((self.canvas.winfo_width(), self.canvas.winfo_height()), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.prediction_label.configure(text="Predictions will be shown here.")

    def recognize_digit(self):
        # Take a screenshot of the canvas area
        filename = f'logs/image_{self.image_number}.png'
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(filename)

        # Process the image for prediction
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        predictions = []

        # Clear existing borders on canvas
        self.canvas.delete("border")

        # Adjust for canvas highlight thickness
        highlight_thickness = int(self.canvas.cget("highlightthickness"))

        for cnt in contours:
            # Calculate bounding rectangle with padding
            x, y, w, h = cv2.boundingRect(cnt)
            padding = 50  # Add some space around the digit
            x_start = max(x - padding, 0)
            y_start = max(y - padding, 0)
            x_end = min(x + w + padding, th.shape[1])
            y_end = min(y + h + padding, th.shape[0])

            # Adjust for highlight thickness
            canvas_x_start = x_start + highlight_thickness
            canvas_y_start = y_start + highlight_thickness
            canvas_x_end = x_end + highlight_thickness
            canvas_y_end = y_end + highlight_thickness

            # Draw the rectangle on the canvas
            self.canvas.create_rectangle(canvas_x_start, canvas_y_start, canvas_x_end, canvas_y_end, outline="red",
                                         width=2, tags="border")

            # Extract and preprocess the ROI
            roi = th[y_start:y_end, x_start:x_end]
            roi = cv2.copyMakeBorder(
                src=roi,
                top=10,
                bottom=10,
                left=10,
                right=10,
                borderType=cv2.BORDER_CONSTANT,
                value=0
            )
            img = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            img = img.reshape(1, 28, 28, 1)
            img = img / 255.0

            # Predict the digit
            pred = model.predict([img])[0]
            final_pred = np.argmax(pred)
            accuracy = int(max(pred) * 100)
            predictions.append(f'Predict {final_pred} [{self.get_digit_label(final_pred)}] {accuracy}%')

        # Update the output section with predictions
        self.prediction_label.configure(text="\n".join(predictions))

    def get_digit_label(self, digit):
        labels = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine"
        }
        return labels.get(digit, "")


if __name__ == "__main__":
    root = ctk.CTk()
    app = DigitRecognitionApp(root)
    root.mainloop()
