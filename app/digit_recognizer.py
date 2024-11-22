import cv2
import numpy as np
from tensorflow.keras.models import load_model


class DigitRecognizer:
    def __init__(self):
        self.model = load_model("models/cnn_model.h5")

    def recognize(self, image_path):
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        predictions = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)

            padding = 60
            x_start, y_start = max(x - padding, 0), max(y - padding, 0)
            x_end, y_end = x + w + padding, y + h + padding

            roi = th[y_start:y_end, x_start:x_end]
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            roi = roi.reshape(1, 28, 28, 1) / 255.0

            pred = self.model.predict(roi)
            predictions.append(f"Predict {np.argmax(pred)} [{int(max(pred[0]) * 100)}%]")

        return predictions
