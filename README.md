# ✋🖌️ HandDrawnDigitAI

Welcome to **HandDrawnDigitAI** – an intuitive app for recognizing hand-drawn digits! Powered by **CustomTkinter**, a pre-trained **Convolutional Neural Network (CNN)**, and a user-friendly **GUI**, this project brings machine learning right to your fingertips. Draw digits, recognize them instantly, and enjoy the seamless experience!

---

## 🗂️ Project Structure

```plaintext
HandDrawnDigitAI/
│
├── app/
│   ├── __init__.py              # Makes `app` a package
│   ├── gui.py                   # Contains the GUI logic
│   ├── digit_recognizer.py      # Logic for recognizing digits
│   ├── themes.py                # Themes dictionary
│   └── utils.py                 # Helper utility functions
│
├── models/
│   └── cnn_model.h5             # Pre-trained model
│
├── logs/                        # Stores temporary image files
│
├── notebooks/
│   └── cnn_mnist.ipynb          # Notebook for model
│
├── run.py                       # Main entry point to the app
├── requirements.txt             # Dependencies for the project
└── README.md                    # Documentation
```
---

## 🚀 Features

- 🖼️ **Interactive Drawing Canvas**  
  Use the mouse to draw digits directly on the canvas.

- 🧠 **AI-Powered Digit Recognition**  
  Recognize digits (0-9) using a **pre-trained CNN model** trained on the **MNIST dataset**.

- 🎨 **Dynamic Themes**  
  Choose from multiple visually appealing themes:  
  🔵 *Oceanic* | 🌙 *Dark Mode* | 🎨 *Vibrant* | 🖤 *Corporate* | 🌸 *Pink Black*

- 🛠️ **Modular Codebase**  
  Clean and organized project structure for easy navigation.

---

## 🎯 How It Works

1. **Draw a digit** on the canvas.  
2. **Press the "Predict" button**, and the model will recognize the digit.  
3. If the prediction isn't clear, **adjust and re-draw** on the canvas!  
4. Use the **"Clear Canvas" button** to start over.

---

## 📋 Requirements

Make sure you have the following dependencies installed before running the app:

```plaintext
tensorflow==2.10.0
customtkinter==5.1.2
pillow==9.2.0
numpy==1.23.0
opencv-python==4.6.0
```

#### Install them using:
```
pip install -r requirements.txt
```

---

## 📂 Files & Directories
### 📁 app/
- **gui.py**  
  Handles the graphical user interface logic, including button interactions and canvas drawing.

- **digit_recognizer.py**  
  Preprocesses the canvas image and uses the CNN model for predictions.

- **themes.py**  
  Stores theme configurations for a visually appealing UI.

- **utils.py**  
  Helper functions to support digit recognition and GUI.
  
### 📁 models/
- **cnn_model.h5**  
  Pre-trained CNN model saved in Keras HDF5 format.

### 📁 logs/
- Temporary directory to store canvas snapshots during runtime.

### 📁 notebooks/
- **cnn_mnist.ipynb**  
  A Jupyter Notebook used to train the CNN model on the MNIST dataset.

### `run.py`
- The main entry point to launch the application.

---

## 🖥️ Running the Application
Follow these steps to get started:

1. Clone the repository:

```
git clone https://github.com/asRot0/HandDrawnDigitAI.git
cd HandDrawnDigitAI
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```
3. Run the app:

```
python run.py
```
4. Draw digits and enjoy the magic! ✨

---
## 🎨 Themes Preview

| 🌙 Dark Mode | 🔵 Oceanic | 🌸 Pink Black |
|:------------:|:----------:|:-------------:|
| ![Dark Mode](https://via.placeholder.com/200/333333/00FF00?text=Dark+Mode) | ![Oceanic](https://via.placeholder.com/200/E0FFFF/1E90FF?text=Oceanic) | ![Pink Black](https://via.placeholder.com/200/FFC0CB/FF007F?text=Pink+Black) |


### 🌸 *`BlackPink`* Theme
![themes](themes/pic1.png)

---

## 🔢 Key Math Concepts for CNN & MNIST

Here are some important mathematical formulas used in this project

### **1️⃣ Convolution Operation (Feature Extraction in CNN)**
Convolutional layers apply filters to extract features from input images.

$$
\LARGE O(i, j) = \sum_m \sum_n I(i+m, j+n) \cdot K(m, n)
$$

- **\( O(i, j) \)** → Output feature map at position \( (i, j) \).  
- **\( I(i+m, j+n) \)** → Input image pixels affected by the filter.  
- **\( K(m, n) \)** → Kernel (filter) values applied to the input.  

📌 **Why Add?**
- Represents how a **filter (kernel) slides over an image** to extract meaningful features.
- Core operation in **Convolutional Neural Networks (CNNs)**.

---

### **2️⃣ ReLU Activation Function (Hidden Layers)**
ReLU introduces non-linearity to the model by keeping only positive values.

$$
\LARGE \text{ReLU}(x) = \max(0, x)
$$

- **\( x \)** → Input value to the activation function.  

📌 **Why Add?**
- Helps **prevent vanishing gradients**.
- Improves CNN’s ability to learn complex patterns.

---

### **3️⃣ Max Pooling (Dimensionality Reduction)**
Max pooling reduces the spatial size of feature maps while preserving key information.

$$
\LARGE P(i, j) = \max_{(m,n) \in R} F(i+m, j+n)
$$

- **\( P(i, j) \)** → Pooled output value at position \( (i, j) \).  
- **\( F(i+m, j+n) \)** → Input feature map values in the pooling region.  
- **\( R \)** → Pooling region (e.g., 2×2 or 3×3 window).  

📌 **Why Add?**
- Reduces computation and prevents **overfitting**.
- Keeps **dominant features** while discarding unnecessary details.

---

### **4️⃣ Softmax Function (Final Layer for Classification)**
The softmax function converts model outputs into probability distributions.

$$
\LARGE \text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{n} e^{z_j}}
$$

- **\( z_i \)** → Raw score (logit) for class \( i \).  
- **\( e^{z_i} \)** → Exponential of the logit, ensuring positive values.  
- **\( \sum_{j=1}^{n} e^{z_j} \)** → Sum of exponentials across all \( n \) classes (normalization factor).  

📌 **Why Add?**
- Softmax assigns **probabilities to digit classes (0-9)**.
- Ensures outputs sum up to **1**, making it interpretable.

---

### **5️⃣ Cross-Entropy Loss (Training the CNN)**
Cross-entropy measures the difference between predicted and actual labels.

$$
\LARGE \mathcal{L} = -\sum_{i=1}^{n} y_i \log(\hat{y_i})
$$

- **\( \mathcal{L} \)** → Cross-entropy loss value.  
- **\( y_i \)** → Actual label (ground truth) for class \( i \) (1 for correct class, 0 otherwise).  
- **\( \hat{y_i} \)** → Predicted probability from the softmax function.  

📌 **Why Add?**
- Penalizes incorrect predictions by increasing the loss.
- Common **loss function** for **multi-class classification**.

---

### **6️⃣ Adam Optimizer (Gradient Descent for CNN Training)**
Adam adjusts learning rates based on gradients to optimize CNN performance.

$$
\LARGE \theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{v_t} + \epsilon} m_t
$$

- **\( \theta_t \)** → Model parameters at step \( t \).  
- **\( m_t \)** → First moment estimate (mean of gradients).  
- **\( v_t \)** → Second moment estimate (variance of gradients).  
- **\( \eta \)** → Learning rate (step size).  
- **\( \epsilon \)** → Small constant to avoid division by zero.  

📌 **Why Add?**
- Used as the **optimizer** in this project (`optimizer='adam'`).
- Combines **momentum & adaptive learning rates** for faster convergence.

These mathematical concepts power the **CNN architecture** used in this project. They help in **feature extraction, classification, optimization, and learning** to recognize hand-drawn digits **efficiently and accurately**.  

---

## 📖 Model Training (Optional)
If you'd like to retrain the model:

1. Open the Jupyter Notebook in the `notebooks`/ directory.
2. Train the CNN on the MNIST dataset.
3. Save the updated model as cnn_model.h5 in the models/ directory.

## 💡 Future Enhancements
- ✍️ Add support for multiple languages.
- 📊 Integrate visualization of model predictions (e.g., activation maps).
- 🔄 Real-time digit recognition with camera input.

---

## 🌟 Contributors
- Asif Ahmed – [GitHub](https://github.com/asRot0/)  
Creator and Maintainer

Want to contribute? Feel free to fork the repository and open a pull request!

## 🤝 Support
If you find this project helpful, consider giving it a ⭐ on [GitHub](https://github.com/asRot0/HandDrawnDigitAI) and sharing it with others!

---