# car-price-predictior

A real-world machine learning application that predicts used car prices based on vehicle features such as manufacturer, year of manufacture, mileage, and fuel type.

---

## 📌 Project Description

The second-hand car market often suffers from inconsistent and subjective pricing. This project addresses that problem by using **Artificial Intelligence and Machine Learning** to provide accurate, data-driven price predictions for used cars.

The system is built using regression-based machine learning models trained on historical car data and deployed through a simple web interface.

This project was developed as part of **Option B: Building a Real-World AI Application**.

---

## 🎯 Objectives

- Analyze a real-world used car dataset  
- Clean and preprocess raw data for model training  
- Train multiple machine learning regression models  
- Evaluate and compare model performance  
- Deploy an interactive application for car price prediction

---

## 📊 Dataset

The dataset contains information about used cars with the following attributes:
- Car name
- Manufacturer
- Year of manufacture
- Kilometers driven
- Fuel type
- Price (target variable)

All features are preprocessed and encoded into numerical formats before training.

---

## 🧠 Machine Learning Models Used

- Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor

### Evaluation Metrics

- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- R² Score

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Backend API:** FastAPI  
- **Web Interface:** Streamlit  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure

```text
car-price-predictior/
│── data/                 # Dataset files
│── notebooks/            # EDA and experiments
│── models/               # Trained models
│── app.py                # Streamlit application
│── requirements.txt      # Project dependencies
│── README.md             # Project documentation
```
```bash
git clone https://github.com/Juniorbarry26/car-price-predictior.git
cd car-price-predictior
```

- pip install -r requirements.txt

