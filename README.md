# 🩺 Disease Prediction System

The **Disease Prediction System** is a machine learning-powered web application that predicts the likelihood of **Diabetes**, **Heart Disease**, and **Parkinson's Disease** based on user-provided health data. Built using **Streamlit** for an intuitive user interface, this project leverages pre-trained models for accurate and fast health predictions.

---

## 🚀 Features
- **Multi-Disease Prediction:** Detects the risk of Diabetes, Heart Disease, and Parkinson's Disease.
- **Interactive Web Interface:** Simple, user-friendly interface built with **Streamlit**.
- **Real-Time Predictions:** Get instant results after inputting your health data.
- **Pre-trained Models:** Efficient models trained on real-world datasets.
- **Lightweight & Fast:** Optimized for performance with quick load times.

---

## 🖥️ Demo

To run the application locally:

```bash
streamlit run app.py
```

_Add a GIF or screenshot of your app in action here._

---

## 📂 Project Structure

```
Disease_Prediction_System/
│
├── datasets/               # Contains datasets for Diabetes, Heart Disease, and Parkinson's
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
│
├── models/                 # Pre-trained ML models saved in .sav format
│   ├── diabetes_model.sav
│   ├── heart_model.sav
│   └── parkinsons_model.sav
│
├── notebooks/              # Jupyter Notebooks for data analysis & model training
│   ├── Diabetes_Prediction.ipynb
│   ├── Heart_Disease_Prediction.ipynb
│   └── Parkinsons_Prediction.ipynb
│
├── app.py                  # Streamlit application code
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation (this file)
```

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** for creating the interactive web app
- **Scikit-learn** for model building and evaluation
- **Pandas** & **NumPy** for data manipulation
- **Matplotlib** & **Seaborn** for data visualization
- **Pickle** for saving and loading machine learning models

---

## 📊 How It Works

1. **Data Collection & Preprocessing:**
   - The datasets for Diabetes, Heart Disease, and Parkinson's Disease are loaded and preprocessed to handle missing values and normalize features.

2. **Model Training:**
   - Different machine learning algorithms (like Logistic Regression, Random Forest, etc.) are applied to train models for each disease.
   - The best-performing models are saved as `.sav` files using `pickle`.

3. **Web Application (Streamlit):**
   - The app takes user inputs through an intuitive form.
   - Based on user inputs, the corresponding pre-trained model predicts whether the user is at risk for the selected disease.
   - The result is displayed instantly.

---

## 📥 Installation Guide

Follow these steps to set up and run the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Harrishdevaraj21/Disease_Prediction_System.git
   cd Disease_Prediction_System
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

---

## 🧪 Example Usage

1. Launch the Streamlit app.
2. Choose the disease you want to predict from the sidebar.
3. Fill in the required health metrics (like glucose level for diabetes, etc.).
4. Click **Predict** to see the result.

---

## 📸 Screenshots
![Screenshot 2025-02-04 154132](https://github.com/user-attachments/assets/745c587c-b77a-4b2a-a612-ca0964ca75a7)
![Screenshot 2025-02-04 154219](https://github.com/user-attachments/assets/5bbdb7b7-b116-4ea5-b5da-1c333cf828d0)
![Screenshot 2025-02-04 154154](https://github.com/user-attachments/assets/75cc4431-ca76-4f20-bd8e-b45c2c3d4a14)



## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the project.
2. **Clone** your fork:
   ```bash
   git clone https://github.com/your-username/Disease_Prediction_System.git
   ```
3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature-name
   ```
4. **Make your changes** and commit:
   ```bash
   git commit -m "Add a meaningful message"
   ```
5. **Push** to your branch:
   ```bash
   git push origin feature-name
   ```
6. **Open a Pull Request** and describe the changes.

---



## 🙌 Acknowledgements

- Datasets sourced from open health data repositories.
- Inspired by modern healthcare prediction systems.

---
