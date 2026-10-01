import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Unemployment in India.csv")

print(df.head())
print(df.columns)
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())
df = pd.read_csv("Unemployment in India.csv")
# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nCleaned Column Names:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nRows containing missing values:")
print(df[df.isnull().any(axis=1)])



df = pd.read_csv("Unemployment in India.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nCleaned Column Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nRows containing missing values:")
print(df[df.isnull().any(axis=1)])

# Remove rows where all values are missing
df.dropna(how='all', inplace=True)

print("\nShape after removing empty rows:")
print(df.shape)

print("\nMissing Values after cleaning:")
print(df.isnull().sum())
print("\nData Types:")
print(df.dtypes)
# Convert numerical columns to numeric data type
df['Estimated Unemployment Rate (%)'] = pd.to_numeric(
    df['Estimated Unemployment Rate (%)'], errors='coerce'
)

df['Estimated Employed'] = pd.to_numeric(
    df['Estimated Employed'], errors='coerce'
)

df['Estimated Labour Participation Rate (%)'] = pd.to_numeric(
    df['Estimated Labour Participation Rate (%)'], errors='coerce'
)

print("\nData Types after conversion:")
print(df.dtypes)
print("\nMissing Values after data type conversion:")
print(df.isnull().sum())
print("\nStatistical Summary:")
print(df.describe())
# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print("\nDate Data Type:")
print(df['Date'].dtype)

print("\nDate Range:")
print(df['Date'].min(), "to", df['Date'].max())
# Calculate monthly average unemployment rate
monthly_unemployment = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

print("\nMonthly Average Unemployment Rate:")
print(monthly_unemployment)
# Plot monthly average unemployment rate

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_unemployment.index,
    monthly_unemployment.values,
    marker='o'
)

plt.title('Monthly Average Unemployment Rate')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
# Average unemployment rate by area
area_unemployment = df.groupby('Area')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by Area:")
print(area_unemployment)
# Plot average unemployment rate by area
plt.figure(figsize=(8, 5))

area_unemployment.plot(kind='bar')

plt.title('Average Unemployment Rate by Area')
plt.xlabel('Area')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
# COVID-19 period analysis

df['Period'] = df['Date'].apply(
    lambda x: 'Before COVID-19' if x < pd.Timestamp('2020-03-01')
    else 'During COVID-19'
)

covid_analysis = df.groupby('Period')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate: Before vs During COVID-19")
print(covid_analysis)
# Plot COVID-19 period comparison
plt.figure(figsize=(8, 5))

covid_analysis.plot(kind='bar')

plt.title('Average Unemployment Rate: Before vs During COVID-19')
plt.xlabel('Period')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
# Monthly unemployment pattern

df['Month'] = df['Date'].dt.month_name()

monthly_pattern = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by Month:")
print(monthly_pattern)
# Plot monthly unemployment pattern
plt.figure(figsize=(10, 5))

monthly_pattern.plot(kind='bar')

plt.title('Average Unemployment Rate by Month')
plt.xlabel('Month')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
# Average unemployment rate by region
region_unemployment = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by Region:")
print(region_unemployment)

# Plot average unemployment rate by region
plt.figure(figsize=(12, 6))

region_unemployment.sort_values(ascending=False).plot(kind='bar')

plt.title('Average Unemployment Rate by Region')
plt.xlabel('Region')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
# Highest and lowest average unemployment rate by region

highest_region = region_unemployment.idxmax()
highest_rate = region_unemployment.max()

lowest_region = region_unemployment.idxmin()
lowest_rate = region_unemployment.min()

print("\nHighest Average Unemployment Rate:")
print(highest_region, ":", highest_rate, "%")

print("\nLowest Average Unemployment Rate:")
print(lowest_region, ":", lowest_rate, "%")
# Key insights from the analysis

print("\n========== KEY INSIGHTS ==========")

print(
    "1. The average unemployment rate in urban areas "
    "was higher than in rural areas."
)

print(
    "2. The unemployment rate increased sharply during "
    "April and May 2020."
)

print(
    "3. The highest monthly average unemployment rate "
    "was observed in May 2020."
)

print(
    "4. The dataset shows a clear change in unemployment "
    "levels during the COVID-19 period."
)

print(
    "5. Unemployment rates varied across different regions."
)
# Final dataset verification

print("\n========== FINAL DATASET CHECK ==========")

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nFinal columns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nFinal data types:")
print(df.dtypes)