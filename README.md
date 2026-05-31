# 🚗 Used Car Price Prediction

A Machine Learning-based web application that predicts the resale value of used cars using features such as company, model, manufacturing year, kilometers driven, and fuel type. The project is built using **Python**, **Scikit-Learn**, and **Streamlit**, and deployed as an interactive web application.

## 🌐 Live Demo

**Try the application here:**

[Live App Demo](https://car-price-prediction-model-20-ggdrkxknfp5bsjdukiqxln.streamlit.app/?utm_source=chatgpt.com)

---

## 📌 Project Overview

Buying or selling a used car often involves uncertainty regarding its fair market value. This project aims to solve that problem by leveraging Machine Learning to estimate a car's resale price based on historical vehicle data.

The model learns patterns from various car attributes and predicts a realistic resale price instantly through a user-friendly web interface.

---

## ✨ Features

* Predict used car resale prices instantly
* Interactive Streamlit web interface
* Dynamic filtering of car models based on selected company
* Fuel type filtering based on selected vehicle
* Random Forest Regression model
* Clean and responsive UI
* Real-time predictions

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit

### Machine Learning

* Random Forest Regressor
* One-Hot Encoding
* Pipeline Architecture

---

## 📊 Input Features

The model uses the following features:

| Feature           | Description               |
| ----------------- | ------------------------- |
| Company           | Car manufacturer          |
| Model Name        | Vehicle model             |
| Year              | Manufacturing year        |
| Kilometers Driven | Total distance driven     |
| Fuel Type         | Petrol, Diesel, LPG, etc. |

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Handling Missing Values
4. Feature Engineering
5. One-Hot Encoding of Categorical Features
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Serialization using Joblib
10. Streamlit Deployment

---

## 📈 Model Performance

| Model                   | R² Score |
| ----------------------- | -------- |
| Linear Regression       | 0.86     |
| KNN Regressor           | 0.81     |
| Random Forest Regressor | ~0.90    |

Random Forest Regressor achieved the best performance and was selected for deployment.

---

## 📂 Project Structure

```bash
car-price-prediction/
│
├── app.py
├── model.ipynb
├── car_price.csv
├── clean_car_price_data.csv
├── car_price_rf_model.pkl
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/used-car-price-prediction.git
```

Move to the project directory:

```bash
cd used-car-price-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

Add screenshots of:

* Home Page
* Input Form
* Prediction Result Page

inside the repository's `assets/` folder and link them here.

---

## 🎯 Future Improvements

* Feature Importance Visualization
* Hyperparameter Tuning Dashboard
* Model Explainability using SHAP
* Price Trend Analytics
* Car Recommendation System
* Cloud Database Integration

---

## 👨‍💻 Author

**Anuj**

AIML Undergraduate | Machine Learning Enthusiast | DSA Learner

---

## ⭐ Support

If you found this project useful, consider giving the repository a star. It helps showcase the project and supports future development.
