from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__, template_folder='static/templates')

# Load model and dataset
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')


@app.route('/')
def index():
    # Clean columns to avoid float vs string issues
    companies = sorted(car['company'].dropna().astype(str).unique())
    car_models = sorted(car['name'].dropna().astype(str).unique())
    years = sorted(car['year'].dropna().astype(int).unique(), reverse=True)
    fuel_types = sorted(car['fuel_type'].dropna().astype(str).unique())

    return render_template(
        "index.html",
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_types=fuel_types
    )


@app.route('/predict', methods=['POST'])
def predict():
    try:
        company = request.form.get('company')
        car_model = request.form.get('car_models')
        fuel_type = request.form.get('fuel_type')
        year = request.form.get('year')
        kms_driven = request.form.get('kilo_driven')

        if not all([company, car_model, fuel_type, year, kms_driven]):
            return "Prediction error: Missing input fields", 400

        # Convert to proper types
        year = int(float(year))
        kms_driven = int(float(kms_driven))

        # Create DataFrame with correct column names for the model
        input_df = pd.DataFrame(
            [[car_model, company, year, kms_driven, fuel_type]],
            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']  # <-- lowercase 'year'
        )

        # Predict
        prediction = model.predict(input_df)

        # Convert Dalasis -> USD
        exchange_rate = 0.019
        prediction_usd = round(float(prediction[0]) * exchange_rate, 2)

        return str(prediction_usd)

    except Exception as e:
        return f"Prediction error: {str(e)}", 400


if __name__ == '__main__':
    app.run(debug=True)
