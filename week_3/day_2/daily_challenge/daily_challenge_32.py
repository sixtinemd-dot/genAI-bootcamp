import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA

# 1. Load dataset
ds = pd.read_csv("/Users/sixtinemauchard/Downloads/genAI-bootcamp/week_3/day_2/daily_challenge/datascience_salaries.csv")

# 2. Basic exploration
print("First 5 rows:")
print(ds.head())

print("\nColumns:")
print(ds.columns)

print("\nMissing values:")
print(ds.isnull().sum())

# 3. Normalize the 'salary' column using Min-Max normalization
salary_scaler = MinMaxScaler()
ds['salary_normalized'] = salary_scaler.fit_transform(ds[['salary']])

print("\nSalary normalization preview:")
print(ds[['salary', 'salary_normalized']].head())

# 4. Prepare data for PCA
# Convert categorical columns into numeric columns
ds_pca = pd.get_dummies(ds, drop_first=True)

# Drop original salary column 
X = ds_pca.drop(columns=['salary'], errors='ignore')

# Standardize features before PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

pca_ds = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])

print("\nPCA result (first 5 rows):")
print(pca_ds.head())

print("\nExplained variance ratio:")
print(pca.explained_variance_ratio_)

# 6. Group by experience_level and calculate average and median salary
salary_summary = ds.groupby('experience_level')['salary'].agg(
    average_salary='mean',
    median_salary='median'
).reset_index()

print("\nSalary summary by experience level:")
print(salary_summary)