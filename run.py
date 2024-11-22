from customtkinter import CTk
from app.gui import DigitRecognitionApp

if __name__ == "__main__":
    root = CTk()
    app = DigitRecognitionApp(root)
    root.mainloop()
