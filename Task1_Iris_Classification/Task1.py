import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Convert dataset into a DataFrame
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Add flower species
df["Species"] = iris.target_names[iris.target]

# Display first five rows
print("First 5 Rows of Iris Dataset:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)
# Select features and target

X = df.drop("Species", axis=1)
y = df["Species"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())
# Split the data into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)
# Train the Logistic Regression model

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=200)

model.fit(X_train, y_train)

print("\nModel trained successfully!")
# Evaluate model accuracy

from sklearn.metrics import accuracy_score
# Make predictions

y_pred = model.predict(X_test)

print("\nPredicted Values:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)
# Classification report

from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
# Create confusion matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)
# Visualize confusion matrix

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))

plt.imshow(cm)

plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.xticks(
    range(3),
    iris.target_names
)

plt.yticks(
    range(3),
    iris.target_names
)

plt.colorbar()

plt.show()