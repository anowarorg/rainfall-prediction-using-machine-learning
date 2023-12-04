from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

rfr = joblib.load('predict_rainfall_model.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_rainfall_endpoint():
    data = request.json
    features = [data['Month'], data['Min Temp 0 C'], data['Relative Humidity %'], data['Wind Speed (m/s)'],
                data['Cloud Coverage %'], data['Bright Sunshine (Hours)'], data['Station Number']]
    
    # Convert features to DataFrame for predict_rainfall function
    user_input = pd.DataFrame([features], columns=['Month', 'Min Temp 0 C', 'Relative Humidity %', 'Wind Speed (m/s)',
                                                   'Cloud Coverage %', 'Bright Sunshine (Hours)', 'Station Number'])
    
    # Make predictions using the Random Forest model
    rainfall_prediction = rfr.predict(user_input)

    return jsonify({'predicted_rainfall': rainfall_prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
