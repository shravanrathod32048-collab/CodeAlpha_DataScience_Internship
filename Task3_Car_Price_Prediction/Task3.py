import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("car data.csv")

print(df.head())
print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())
print("\nStatistical Summary:")
print(df.describe())
print("\nFuel Types:")
print(df['Fuel_Type'].value_counts())

print("\nSelling Types:")
print(df['Selling_type'].value_counts())

print("\nTransmission Types:")
print(df['Transmission'].value_counts())

print("\nOwner Types:")
print(df['Owner'].value_counts())


# Remove Car_Name and separate target variable
X = df.drop(['Selling_Price', 'Car_Name'], axis=1)
y = df['Selling_Price']

# Convert categorical columns into numerical values
X = pd.get_dummies(
    X,
    columns=['Fuel_Type', 'Selling_type', 'Transmission'],
    drop_first=True
)

print("\nFeatures after encoding:")
print(X.head())

print("\nData types after encoding:")
print(X.dtypes)

print("\nShape of X:", X.shape)
print("Shape of y:", y.shape)
from sklearn.model_selection import train_test_split

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:")
print(X_train.shape)

print("\nTesting data shape:")
print(X_test.shape)

print("\nTraining target shape:")
print(y_train.shape)

print("\nTesting target shape:")
print(y_test.shape)
from sklearn.linear_model import LinearRegression

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel training completed successfully!")
# Make predictions on the test data
y_pred = model.predict(X_test)

print("\nActual Selling Prices:")
print(y_test.values)

print("\nPredicted Selling Prices:")
print(y_pred)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)
# Plot actual vs predicted selling prices

plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.title("Actual vs Predicted Car Prices")

plt.tight_layout()
plt.show()
# Compare actual and predicted prices

comparison = pd.DataFrame({
    'Actual Price': y_test.values,
    'Predicted Price': y_pred
})

print("\n========== ACTUAL VS PREDICTED PRICES ==========")
print(comparison.head(10))
# Analyze feature coefficients

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})

feature_importance['Absolute_Coefficient'] = (
    feature_importance['Coefficient'].abs()
)

feature_importance = feature_importance.sort_values(
    by='Absolute_Coefficient',
    ascending=False
)

print("\n========== FEATURE IMPORTANCE ==========")
print(feature_importance)
# Final Actual vs Predicted Price Visualization

plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred)

# Reference line: perfect predictions
min_price = min(y_test.min(), y_pred.min())
max_price = max(y_test.max(), y_pred.max())

plt.plot(
    [min_price, max_price],
    [min_price, max_price],
    linestyle='--'
)

plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.title("Actual vs Predicted Car Selling Prices")

plt.tight_layout()
plt.show()
print("\n========== FINAL PROJECT CHECK ==========")

print("Dataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nFeatures used by model:")
print(X.columns.tolist())

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nR² Score:", r2)
print("MAE:", mae)
print("MSE:", mse)

print("\nTask 3 completed successfully!")