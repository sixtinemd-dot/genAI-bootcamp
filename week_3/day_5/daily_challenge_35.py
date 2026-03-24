import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
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
# Sales by year
df["Year"] = df["Order Date"].dt.year
sales_trend = df.groupby("Year")["Sales"].sum()

fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(sales_trend.index, sales_trend.values, marker="o")

ax.set_title("Interactive Sales Trend Over Years")
ax.set_xlabel("Year")
ax.set_ylabel("Total Sales")
ax.grid(True)

# Add hover interaction
cursor = mplcursors.cursor(line, hover=True)
@cursor.connect("add")
def on_add(sel):
    x, y = sel.target
    sel.annotation.set_text(f"Year: {int(round(x))}\nSales: {y:,.2f}")

plt.show()

#map
# grouped by city
city_sales = df.groupby(["City", "State"])["Sales"].sum().reset_index()

# Show top cities instead of map
top_cities = city_sales.sort_values(by="Sales", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_cities["City"], top_cities["Sales"])

plt.title("Top Cities by Sales (No Geographic Coordinates Available)")
plt.xlabel("Sales")
plt.ylabel("City")

plt.show()

#important commment :
""" The dataset does not include geographic coordinates such as latitude and longitude, which are required to create a true map visualization in Matplotlib. Therefore, a bar chart of top cities by sales is used as an alternative representation of geographic distribution. """

#3. Data Visualization with Seaborn:
#bar chart
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_products,
    x="Sales",
    y="Product Name",
    hue="Product Name",
    palette="Blues_d",
    legend=False
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
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


