# Task 3 – Car Price Prediction with Machine Learning

## 📌 Project Overview

This project predicts the selling price of used cars using Machine Learning. The analysis uses features such as present price, manufacturing year, kilometers driven, fuel type, selling type, transmission, and previous ownership.

The project was completed as part of the **CodeAlpha Data Science Internship**.

## 🎯 Objectives

- Analyze used car data.
- Perform data cleaning and preprocessing.
- Convert categorical variables into numerical features.
- Select relevant features for prediction.
- Train a Machine Learning regression model.
- Predict car selling prices.
- Evaluate model performance using regression metrics.
- Visualize actual and predicted prices.

## 📂 Dataset

**Dataset:** `car data.csv`

### Main Columns

- `Car_Name` – Name of the car
- `Year` – Manufacturing year
- `Selling_Price` – Selling price of the car
- `Present_Price` – Current market price
- `Driven_kms` – Kilometers driven
- `Fuel_Type` – Fuel type
- `Selling_type` – Type of seller
- `Transmission` – Transmission type
- `Owner` – Number of previous owners

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## 🔄 Project Workflow

1. Load the car dataset using Pandas.
2. Inspect the dataset and its data types.
3. Check for missing values and duplicate records.
4. Separate input features and target variable.
5. Remove `Car_Name` from the prediction features.
6. Encode categorical variables using One-Hot Encoding.
7. Split the dataset into training and testing sets.
8. Train a Linear Regression model.
9. Generate car price predictions.
10. Evaluate the model using R², MAE, and MSE.
11. Visualize actual vs predicted prices.

## 🤖 Machine Learning Model

The project uses **Linear Regression** to predict the `Selling_Price` of cars.

### Target Variable

`Selling_Price`

### Important Features

- `Year`
- `Present_Price`
- `Driven_kms`
- `Fuel_Type`
- `Selling_type`
- `Transmission`
- `Owner`

## 📊 Model Performance

The Linear Regression model achieved:

- **R² Score:** 0.8489
- **R² Percentage:** 84.89%
- **MAE:** 1.2164
- **MSE:** 3.4813

The model was evaluated on the test dataset using predictions generated from previously unseen test data.

## 📈 Visualizations

The project includes:

- Actual vs Predicted Selling Price
- Actual vs Predicted Price with a reference line
- Feature coefficient visualization

## 💡 Key Learning Outcomes

Through this project, I gained practical experience in:

- Regression problems
- Data preprocessing
- One-Hot Encoding
- Feature selection
- Train-test splitting
- Linear Regression
- Model evaluation
- Data visualization
- Interpreting Machine Learning results

## ▶️ How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```

3. Place `Task3.py` and `car data.csv` in the same folder.
4. Run:

```bash
python Task3.py
```

## 👨‍💻 Internship

**CodeAlpha Data Science Internship – Task 3**

Project: **Car Price Prediction with Machine Learning**
