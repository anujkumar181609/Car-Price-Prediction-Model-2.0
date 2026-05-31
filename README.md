# 🚗 Used Car Price Prediction

A Machine Learning-powered web application that predicts the resale value of used cars based on vehicle specifications such as company, model, manufacturing year, fuel type, and kilometers driven.

## 🌐 Live Demo

👉 https://car-price-prediction-model-20-ggdrkxknfp5bsjdukiqxln.streamlit.app/

---

## 📌 Project Overview

Buying or selling a used car often involves uncertainty regarding its fair market value. This project aims to solve that problem by leveraging Machine Learning algorithms to estimate a vehicle's resale price accurately.

The application is built using:

- Python
- Pandas
- Scikit-Learn
- XGBoost
- Streamlit

Users can enter vehicle details through an intuitive web interface and instantly receive a predicted resale price.

---

## 🎯 Objective

The primary objective of this project is to:

- Predict used car resale prices accurately.
- Compare multiple Machine Learning algorithms.
- Deploy the best-performing model as a web application.
- Provide a user-friendly interface for real-time predictions.

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Linear Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

### Deployment
- Streamlit

---

## 📂 Features Used

The model predicts car prices using:

| Feature | Description |
|----------|-------------|
| Company | Car manufacturer |
| Name | Car model |
| Year | Manufacturing year |
| Kms Driven | Total distance driven |
| Fuel Type | Petrol, Diesel, LPG, etc. |

---

## ⚙️ Data Preprocessing

The dataset was cleaned and preprocessed before training:

- Removed null values
- Cleaned inconsistent entries
- Converted numerical columns into proper formats
- Handled outliers
- Encoded categorical features using One-Hot Encoding
- Created an end-to-end ML pipeline for preprocessing and prediction

---

## 📊 Model Performance Comparison

| Model | R² Score | MAE | RMSE |
|---------|---------|---------|---------|
| Linear Regression | 0.8585 | 68,642 | 119,669 |
| KNN | 0.8116 | 90,051 | 138,100 |
| SVM | -0.0343 | 197,735 | 323,578 |
| Decision Tree | 0.7568 | 81,910 | 156,892 |
| XGBoost | 0.8520 | 73,309 | 122,396 |
| **Random Forest** ⭐ | **0.9010** | **62,918** | **100,131** |

### 🏆 Best Model

**Random Forest Regressor** achieved the highest R² score and lowest prediction error among all tested models.

Therefore, Random Forest was selected for deployment.

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Selection
8. Deployment with Streamlit

---

## 🚀 How to Run Locally

### Clone Repository

```bash
git clone https://github.com/yourusername/used-car-price-prediction.git
```

### Move into Project Directory

```bash
cd used-car-price-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
├── app.py
├── model.ipynb
├── car_price.csv
├── clean_car_price_data.csv
├── car_price_rf_model.pkl
├── requirements.txt
└── README.md
```

---

## 📸 Application Preview

### Input Parameters

- Company
- Model
- Manufacturing Year
- Kilometers Driven
- Fuel Type

### Output

- Predicted Resale Price (₹)

---

## 💡 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Feature importance visualization
- Price trend analysis
- Integration with live automobile market datasets
- Model explainability using SHAP

---

## 👨‍💻 Author

**Anuj**

Artificial Intelligence & Machine Learning Student

Passionate about Machine Learning, Data Structures & Algorithms, and Building Real-World AI Applications.

---

## ⭐ If you found this project useful, consider giving it a star!
