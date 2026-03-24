import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#1. Data Preparation:

# Load dataset
df = pd.read_excel('/Users/sixtinemauchard/Downloads/genAI-bootcamp/week_3/day_5/US_Superstore_data.xls', engine="xlrd")

# Quick check
print(df.head(10))
print(df.info())

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

#2. Data Visualization with Matplotlib:
# Extract year
df["Year"] = df["Order Date"].dt.year

# Group by year
sales_year = df.groupby("Year")["Sales"].sum()

#plot
plt.figure(figsize=(10,6))
plt.plot(sales_year.index, sales_year.values, marker="o")

plt.title("Sales Trend Over the Years")
plt.xlabel("Year")
plt.ylabel("Total Sales")

plt.grid(True)
plt.show()

#map
country_sales = df.groupby("Country")["Sales"].sum()

country_sales.plot(kind="bar", figsize=(6,4))

plt.title("Sales by Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.show()

#3. Data Visualization with Seaborn:
#bar chart
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

top_products = top_products.reset_index()

plt.figure(figsize=(10,6))

sns.barplot(
    data=top_products,
    x="Sales",
    y="Product Name",
    hue="Product Name",
    palette="Blues_d",
    legend=False
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.show()

#scatter plot
plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    alpha=0.6
)

plt.title("Relationship Between Profit and Discount")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.show()

#4. Comparative Analysis:

""" 
Matplotlib provides more control and flexibility, making it suitable for custom and interactive visualizations, but requires more code.

Seaborn is easier to use and produces more visually appealing charts with less code, making it ideal for quick statistical visualizations. """


