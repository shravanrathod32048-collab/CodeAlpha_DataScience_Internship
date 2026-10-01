# CodeAlpha Data Science Internship

Welcome to my **Data Science Internship Projects repository**, completed as part of the **CodeAlpha Data Science Internship**.

This repository contains three end-to-end data science and machine learning projects covering **data cleaning, exploratory data analysis, data visualization, feature preprocessing, classification, regression, model evaluation, and extracting insights from real-world datasets**.

The projects demonstrate my practical application of **Python, Pandas, NumPy, Matplotlib, and Scikit-learn** to solve different data science problems.

---

## 👨‍💻 Internship

**Program:** CodeAlpha Data Science Internship  
**Domain:** Data Science & Machine Learning  
**Language:** Python

---

# 📂 Projects

## 1️⃣ Iris Flower Classification

### 📌 Project Overview

The first project focuses on building a **machine learning classification model** to identify the species of an Iris flower based on its physical measurements.

The Iris dataset contains measurements such as:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The objective is to use these measurements to classify flowers into three species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

### 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

### 🔄 Workflow

1. Load the Iris dataset
2. Explore the dataset
3. Convert the dataset into a Pandas DataFrame
4. Separate input features and target variable
5. Split the data into training and testing datasets
6. Train a classification model
7. Generate predictions
8. Evaluate model performance
9. Analyze classification results
10. Visualize the model results

### 🤖 Machine Learning Model

**Logistic Regression**

The model was trained using the Iris flower measurements and used to predict the flower species on unseen test data.

### 📊 Model Evaluation

Model performance was evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix

---

# 2️⃣ Unemployment Analysis with Python

### 📌 Project Overview

The second project focuses on analyzing unemployment data to understand **unemployment trends, regional differences, and changes during the COVID-19 period**.

The dataset contains unemployment-related information across different regions and time periods in India.

### 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

### 🔄 Data Analysis Workflow

1. Load the unemployment dataset
2. Inspect the dataset structure
3. Identify missing values
4. Remove completely empty rows
5. Clean and convert data types
6. Convert date information into datetime format
7. Explore unemployment statistics
8. Calculate monthly average unemployment
9. Compare Rural and Urban unemployment
10. Analyze unemployment during the COVID-19 period
11. Examine regional patterns
12. Create visualizations
13. Extract meaningful insights

### 🧹 Data Cleaning

The original dataset contained completely empty rows.

After removing these rows, the cleaned dataset contained:

**740 records and 7 columns**

The cleaned dataset contained no remaining missing values in the analyzed columns.

### 📈 Key Analysis

The project examined:

- Overall unemployment rate
- Monthly unemployment trends
- Rural vs Urban unemployment
- Regional unemployment patterns
- COVID-19 period changes

The analysis showed a significant increase in average unemployment during **April and May 2020**, compared with the preceding months.

### 📊 Visualizations

The project includes visualizations for:

- Monthly unemployment trends
- Rural vs Urban unemployment
- Regional unemployment patterns
- COVID-19 period comparison

---

# 3️⃣ Car Price Prediction

### 📌 Project Overview

The third project focuses on predicting the **selling price of used cars using machine learning**.

The objective is to understand how different characteristics of a car influence its selling price and build a regression model capable of predicting the selling price.

### 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

### 📋 Dataset Features

The dataset contains the following features:

- Car Name
- Year
- Present Price
- Driven Kilometers
- Fuel Type
- Selling Type
- Transmission
- Owner
- Selling Price

### 🔄 Machine Learning Workflow

1. Load the car dataset
2. Explore the dataset
3. Check data types
4. Check for missing values
5. Check for duplicate records
6. Separate features and target variable
7. Remove the car name column from model training
8. Encode categorical variables
9. Split the dataset into training and testing sets
10. Train a regression model
11. Generate predictions
12. Evaluate model performance
13. Visualize actual vs predicted prices
14. Analyze feature coefficients

### 🧹 Data Preprocessing

The dataset was checked for:

- Missing values
- Duplicate records
- Numerical features
- Categorical features

Categorical variables such as:

- Fuel Type
- Selling Type
- Transmission

were converted into numerical representations using **One-Hot Encoding**.

The `Car_Name` column was excluded from the model because it represents the individual car name rather than a numerical characteristic directly used in this model.

### 🤖 Machine Learning Model

**Linear Regression**

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

The model was trained on the training dataset and evaluated using previously unseen testing data.

### 📊 Model Performance

The trained model achieved:

**R² Score: 0.8489**

Approximately:

**84.89% R²**

Additional evaluation metrics:

- **MAE:** 1.2164
- **MSE:** 3.4813

### 📈 Visualizations

The project includes:

- Actual vs Predicted Selling Price
- Prediction comparison with a reference line
- Feature coefficient visualization

---

# 🛠️ Technologies & Libraries

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning |
| VS Code | Development environment |
| GitHub | Version control and project portfolio |

---

# 🧠 Skills Demonstrated

## Python

- Python programming fundamentals
- Data structures
- Data handling
- File handling

## Data Analysis

- Data loading
- Data cleaning
- Missing-value handling
- Data type conversion
- Duplicate detection
- Statistical analysis
- Group-based analysis

## Exploratory Data Analysis

- Descriptive statistics
- Trend analysis
- Comparative analysis
- Regional analysis
- Time-based analysis

## Data Visualization

- Line charts
- Scatter plots
- Comparison charts
- Model-result visualization

## Machine Learning

- Train/test splitting
- Feature selection
- Categorical encoding
- Classification
- Regression
- Model prediction
- Model evaluation

## Model Evaluation

- Accuracy
- Classification Report
- Confusion Matrix
- R² Score
- Mean Absolute Error
- Mean Squared Error

---

# 📊 Project Summary

| Project | Type | Main Technique |
|---|---|---|
| Iris Flower Classification | Classification | Logistic Regression |
| Unemployment Analysis | Data Analysis / EDA | Pandas & Matplotlib |
| Car Price Prediction | Regression | Linear Regression |

---

# 🎯 Internship Learning Outcomes

These projects helped me gain practical experience in taking a dataset from the initial stage of **data exploration and cleaning** through **analysis, visualization, machine learning, and model evaluation**.

The internship projects provided hands-on experience with:

- Working with real-world datasets
- Cleaning and preparing data
- Performing exploratory data analysis
- Creating meaningful visualizations
- Preparing data for machine learning
- Building classification models
- Building regression models
- Evaluating machine learning models
- Communicating analytical results

---

# 📁 Repository Structure

```text
CodeAlpha_DataScience_Internship/
│
├── README.md
│
├── Task1_Iris_Classification/
│   ├── Task1.py
│   ├── README.md
│   └── screenshots/
│
├── Task2_Unemployment_Analysis/
│   ├── Task2.py
│   ├── Unemployment in India.csv
│   ├── README.md
│   └── screenshots/
│
└── Task3_Car_Price_Prediction/
    ├── Task3.py
    ├── car data.csv
    ├── README.md
    └── screenshots/
```

---

# 🚀 Conclusion

This repository represents my practical work during the **CodeAlpha Data Science Internship**.

The three projects allowed me to work across different areas of data science, including **exploratory data analysis, data visualization, classification, regression, preprocessing, and model evaluation**.

I am continuing to strengthen my skills in **Python, Data Analysis, Machine Learning, SQL, Pandas, NumPy, and Scikit-learn** through hands-on projects and practical problem solving.

---

## 📌 Internship

**CodeAlpha Data Science Internship**

#CodeAlpha #DataScience #Python #MachineLearning #Pandas #NumPy #Matplotlib #ScikitLearn #DataAnalysis
