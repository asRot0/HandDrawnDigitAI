import customtkinter as ctk
from tkinter import Canvas, ROUND, TRUE
from PIL import ImageGrab
from app.themes import themes
from app.digit_recognizer import DigitRecognizer


class DigitRecognitionApp:
    def __init__(self, root):
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme("green")

        self.root = root
        self.root.title("Digit Recognition App")
        self.root.geometry("800x600")
        self.root.rowconfigure(0, weight=1, uniform="a")
        self.root.columnconfigure(0, weight=7, uniform="a")  # Left column
        self.root.columnconfigure(1, weight=3, uniform="a")  # Right column

        self.lastx, self.lasty = None, None
        self.image_number = 0
        self.colorflag = True

        # Create frames and widgets
        self.setup_frames()

        # Digit recognizer instance
        self.digit_recognizer = DigitRecognizer()

    def setup_frames(self):
        """Setup frames for layout."""
        self.frame_left = ctk.CTkFrame(self.root)
        self.frame_left.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")

        self.frame_right = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame_right.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="nsew")

        # Canvas for drawing
        self.frame_left.rowconfigure(0, weight=1)
        self.frame_left.columnconfigure(0, weight=1)
        self.canvas = Canvas(self.frame_left, bg="#FFFAF1", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.bind("<Button-1>", self.activate_event)

        # Setup the right column
        self.setup_right_column()

    def setup_right_column(self):
        """Setup the right column (output and buttons)."""
        self.output_frame = ctk.CTkFrame(self.frame_right, fg_color="#D3D3D3")
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

        self.btn_predict = ctk.CTkButton(
            self.frame_right,
            text="Predict",
            command=self.recognize_digit,
            width=5,
            height=40,
            corner_radius=20,
            fg_color="#FFC0CB",
            hover_color="#FFB6C1",
            text_color="black",
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
            fg_color="black",
            hover_color="#333333",
            text_color="white",
            font=("Arial", 14, "bold"),
        )
        self.btn_clear.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    def clear_canvas(self):
        self.canvas.delete("all")
        for widget in self.output_frame.winfo_children():
            widget.destroy()

        self.prediction_label.grid(row=0, column=0, padx=2, pady=10, sticky="nsew")

    def recognize_digit(self):
        filename = f'logs/image_{self.image_number}.png'
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(filename)

        predictions = self.digit_recognizer.recognize(filename)
        self.display_predictions(predictions)

    def display_predictions(self, predictions):
        if predictions:
            self.colorflag = True
            selected_theme = "pink_black"

            self.prediction_label.grid_forget()

            for i in predictions:
                current_text_color = themes[selected_theme]["text_colors"][0 if self.colorflag else 1]
                current_bg_color = themes[selected_theme]["bg_colors"][0 if self.colorflag else 1]

                ctk.CTkLabel(
                    self.output_frame,
                    text=i,
                    text_color=current_text_color,
                    fg_color=current_bg_color,
                    anchor="w",
                    padx=5,
                    font=("Arial", 14, "bold")
                ).grid(pady=(0, 3), padx=10, sticky='nsew')

                self.colorflag = not self.colorflag
        else:
            self.prediction_label.configure(text="No digits detected")

    def activate_event(self, event):
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.lastx, self.lasty = event.x, event.y

    def draw_lines(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(
            (self.lastx, self.lasty, x, y),
            width=30, fill="black", capstyle=ROUND, smooth=TRUE, splinesteps=12
        )
        self.lastx, self.lasty = x, y
