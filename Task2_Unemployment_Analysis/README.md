# Task 2 – Unemployment Analysis with Python

## 📌 Project Overview

This project analyzes unemployment trends in India using Python and Pandas. The analysis focuses on unemployment rates across different regions and areas and examines changes over time, including the impact of the COVID-19 period.

The project was completed as part of the **CodeAlpha Data Science Internship**.

## 🎯 Objectives

- Clean and prepare the unemployment dataset.
- Analyze unemployment rates over time.
- Compare unemployment between Rural and Urban areas.
- Analyze monthly unemployment trends.
- Examine unemployment during the COVID-19 period.
- Identify important patterns and insights from the data.
- Create visualizations to communicate the findings.

## 📂 Dataset

**Dataset:** `Unemployment in India.csv`

The dataset contains unemployment information for different regions of India.

### Main Columns

- `Region` – Name of the region
- `Date` – Date of the observation
- `Frequency` – Frequency of the data
- `Estimated Unemployment Rate (%)` – Unemployment rate
- `Estimated Employed` – Estimated number of employed people
- `Estimated Labour Participation Rate (%)` – Labour participation rate
- `Area` – Rural or Urban

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

## 🔄 Project Workflow

1. Load the dataset using Pandas.
2. Inspect the dataset structure and data types.
3. Identify and remove completely empty rows.
4. Handle missing values and convert columns to appropriate data types.
5. Convert the `Date` column into datetime format.
6. Analyze unemployment rates over time.
7. Calculate monthly average unemployment rates.
8. Compare Rural and Urban unemployment.
9. Analyze the COVID-19 period.
10. Create visualizations.
11. Extract key insights from the analysis.

## 📊 Key Results

- The cleaned dataset contains **740 observations**.
- The dataset covers the period from **May 2019 to June 2020**.
- The overall average unemployment rate is approximately **11.79%**.
- The average unemployment rate during the COVID-19 period increased significantly.
- Rural and Urban areas show different unemployment patterns.
- **April and May 2020** recorded particularly high average unemployment rates.

## 📈 Visualizations

The project includes visualizations for:

- Monthly average unemployment rate
- Rural vs Urban unemployment
- COVID-19 period unemployment
- Monthly unemployment patterns

## 💡 Key Learning Outcomes

Through this project, I gained practical experience in:

- Data cleaning
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Date and time analysis
- GroupBy operations in Pandas
- Data visualization
- Extracting insights from real-world datasets

## ▶️ How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

3. Place `Task2.py` and `Unemployment in India.csv` in the same folder.
4. Run the Python file:

```bash
python Task2.py
```

## 👨‍💻 Internship

**CodeAlpha Data Science Internship – Task 2**

Project: **Unemployment Analysis with Python**
