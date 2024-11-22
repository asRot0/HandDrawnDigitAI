import cv2
import numpy as np
from tensorflow.keras.models import load_model


class DigitRecognizer:
    def __init__(self):
        self.model = load_model("models/cnn_model.h5")

    def get_digit_label(self, digit):
        labels = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine"
        }
        return labels.get(digit, "")

    def recognize(self, image_path, canvas):
        self.canvas = canvas
        # Process the image for digit recognition
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        predictions = []
        self.canvas.delete("border")

        for cnt in contours:
            # Calculate bounding rectangle
            x, y, w, h = cv2.boundingRect(cnt)

            # Add padding around the digit
            padding = 60
            x_start = max(x - padding, 0)
            y_start = max(y - padding, 0)
            x_end = min(x + w + padding, th.shape[1])
            y_end = min(y + h + padding, th.shape[0])

            # Draw the rectangle on the canvas
            self.canvas.create_rectangle(
                x_start, y_start, x_end, y_end,
                outline="gray", width=2, tags="border"
            )

            # Extract the region of interest (ROI) for prediction
            roi = th[y_start:y_end, x_start:x_end]
            roi = cv2.copyMakeBorder(
                src=roi,
                top=10, bottom=10, left=10, right=10,
                borderType=cv2.BORDER_CONSTANT, value=0
            )
            img = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            img = img.reshape(1, 28, 28, 1) / 255.0


            # Predict the digit
            pred = self.model.predict([img])[0]
            final_pred = np.argmax(pred)
            accuracy = int(max(pred) * 100)
            predictions.append(f"Predict {final_pred} [{self.get_digit_label(final_pred)}] {accuracy}%")

            # self.prediction_label.configure(text=predictions[-1], fg_color='orange')

        return predictions
