#exercice 1
import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv("/Users/sixtinemauchard/Downloads/genAI-bootcamp/week_3/day_2/exercices_XP/train.csv")

# Number of rows before removing duplicates
rows_before = len(titanic)

# Check for duplicate rows
duplicates = titanic.duplicated()
print("Number of duplicate rows:", duplicates.sum())

# Remove duplicate rows
titanic = titanic.drop_duplicates()

# Number of rows after removing duplicates
rows_after = len(titanic)

print("Rows before removing duplicates:", rows_before)
print("Rows after removing duplicates:", rows_after)

#exercice 2
from sklearn.impute import SimpleImputer

# Identify missing values
print("Missing values per column:")
print(titanic.isnull().sum())

# Strategy 1: Remove the Cabin column (too many missing values)
titanic = titanic.drop(columns=["Cabin"])

# Strategy 2: Fill missing values with a constant
titanic["Embarked"] = titanic["Embarked"].fillna("Unknown")

# Strategy 3: Impute numerical values with the mean
imputer = SimpleImputer(strategy="mean")
titanic["Age"] = imputer.fit_transform(titanic[["Age"]])

# Show the first rows
print("\nDataset after handling missing values:")
print(titanic.head())

#exercice 3

from sklearn.preprocessing import LabelEncoder


# Create Family Size feature
titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"] + 1


# Extract Title from Name
titanic["Title"] = titanic["Name"].str.extract(" ([A-Za-z]+)\.", expand=False)
print(titanic["Title"].unique())

# Encode the Title column (categorical → numerical)
titanic["Title"] = LabelEncoder().fit_transform(titanic["Title"])

# Show result
print(titanic.head())

#exercice 4
import numpy as np
import matplotlib.pyplot as plt

# Fill missing Age values
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

# Visualize outliers
titanic.boxplot(column=["Fare"])
plt.show()

titanic.boxplot(column=["Age"])
plt.show()

# Cap Fare outliers at 98th percentile
cap = titanic["Fare"].quantile(0.98)
titanic["Fare"] = titanic["Fare"].clip(upper=cap)

# Log transform Fare
titanic["Fare_log"] = np.log1p(titanic["Fare"])

# Compare before and after
print(titanic[["Fare","Age","Fare_log"]].describe())

#exercice 5
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Standardize Age
scaler_std = StandardScaler()
titanic["Age_scaled"] = scaler_std.fit_transform(titanic[["Age"]])

# Normalize Fare
scaler_mm = MinMaxScaler()
titanic["Fare_scaled"] = scaler_mm.fit_transform(titanic[["Fare"]])

# Show result
print(titanic[["Age","Age_scaled","Fare","Fare_scaled"]].head())

#exercice 6

# Check remaining categorical columns
print(titanic[["Sex", "Embarked", "Title"]].head())

# Apply One-Hot Encoding
titanic = pd.get_dummies(titanic, columns=["Sex", "Embarked", "Title"], drop_first=True)

# Show result
print(titanic.head())

#exercice 7

# Create age groups
bins = [0, 12, 18, 60, 100]
labels = ["child", "teen", "adult", "senior"]

titanic["AgeGroup"] = pd.cut(titanic["Age"], bins=bins, labels=labels)

# One-hot encode AgeGroup
titanic = pd.get_dummies(titanic, columns=["AgeGroup"], drop_first=True)

# Show result
print(titanic[["Age", "AgeGroup_teen", "AgeGroup_adult", "AgeGroup_senior"]].head())