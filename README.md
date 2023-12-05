# Rainfall Prediction usingm Machine Learning

# Overview:
This Project is mainly based on Rainfall Prediction focusing on Bangladesh. It utilizes machine learning algorithms for long-term rainfall prediction, crucial for agricultural planning and climate-related analysis. The application's has web interface, demonstrates the predictions based on various machine learning models.

# Technologies Used:
1. Scala Programming Language: The primary language used for the project implementation.
2. Apache Spark: Employed for large-scale machine learning, providing a distributed computing framework.
3. HighCharts: Utilized for data visualization, enhancing the user interface.
4. Jupyter Notebook: The interactive environment for developing and presenting the source code.
5. Joblib: Used for saving and loading machine learning models efficiently.
6. Fask: Used Flask.
7. Html, CSS: For making the web Entire face.

# Dataset:
The dataset encompasses weather station and year-wise monthly rainfall data for Bangladesh. The data spans 46 years (1970 to 2016) and includes daily and monthly rainfall data. Relevant columns include Station, Year, Month, and Day (for daily data), among others.

# Models:
1. Linear Regression Model: Utilized for predicting rainfall based on linear relationships between variables.
2. Decision Tree Model: Applied to capture decision rules and predict rainfall in a tree-like structure.
3. Random Forest Model: Employed for ensemble learning, combining multiple decision trees for enhanced accuracy.

# Usage:
Users can interact with the project by accessing the provided web application(Locally hosted). Additionally, the Jupyter Notebook source code, Rainfall_Prediction_Source_Code.ipynb, guides users through the data analysis, preprocessing, and model training process.

# Features:

1. Utilizes machine learning models for rainfall prediction in Bangladesh.
2. Offers a web-based application for interactive exploration of rainfall predictions.
3. Demonstrates the use of Apache Spark and Scala for large-scale machine learning.

# Run Commnads for Running the App:

1. python -m venv venv
2. python -m flask --app .\app.py run
3. .\venv\Scripts\activate.bat
4. python -m pip install --upgrade pip
5. python -m pip install flask
6. python -m flask run
7. python -m pip3 freeze >> requirements.txt

# Conclusion:
This project significantly contributes to rainfall prediction efforts in Bangladesh by applying machine learning models to historical weather data. The predictive models, showcased in the web application, exhibit enhanced accuracy over time, emphasizing the project's success in addressing the vital need for accurate rainfall forecasts in the region. The inclusion of multiple machine learning algorithms and the utilization of Apache Spark showcase the versatility and robustness of the implemented solution.
