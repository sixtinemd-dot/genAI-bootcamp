import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_excel('/Users/sixtinemauchard/Downloads/genAI-bootcamp/week_3/day_5/US_Superstore_data.xls', engine="xlrd")

#Which states have the most sales?
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
print(state_sales)

plt.figure(figsize=(12,7))
plt.bar(state_sales.head(10).index, state_sales.head(10).values, color='steelblue', edgecolor='blue')

plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.xticks(rotation=45, ha='right')
plt.show()

#What is the difference between New York and California in terms of sales and profit? (Compare the total sales and profit between New York and California.)

ny_ca = df[df["State"].isin(["New York", "California"])].groupby("State")[["Sales", "Profit"]].sum()
print(ny_ca)

ny_ca.plot(kind='bar',figsize=(10,6))
    
plt.title('Total Sales and Profit: NY vs CA')
plt.xlabel('State')
plt.ylabel('Amount')
plt.xticks(rotation=0)
plt.show()

#Who is an outstanding customer in New York?
ny_customers = (
    df[df["State"] == "New York"]
    .groupby("Customer Name")[["Sales", "Profit"]]
    .sum()
    .sort_values(by="Sales", ascending=False)
)

print("Top customer in New York by sales and proft:")
print(ny_customers.head(1))


#Are there any differences among states in profitability?

state_profit = df.groupby('State')['Profit'].sum().sort_values(ascending=False).reset_index()
max_profits = state_profit.head(10)
min_profit = state_profit.tail(10)

print(max_profits)
print()
print(min_profit)

sns.barplot(data=max_profits, x='State', y= 'Profit')

plt.title('Highest profit by state')
plt.xticks(rotation=45)
plt.show()

sns.barplot(data=min_profit, x='State', y= 'Profit')

plt.title('Lowest profit by state')
plt.xticks(rotation=45)
plt.show()

#What are the Top 20 cities by Sales ? What about the Top 20 cities by Profit ? Are there any difference among cities in profitability ? (Identify the top 20 cities based on total sales and total profit and analyze differences in profitability among these cities.)

city_profit = df.groupby('City')['Profit'].sum().sort_values(ascending=False).reset_index()
max_profit = city_profit.head(20)
print(max_profit)
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).reset_index()
max_sales = city_sales.head(20)
print(max_sales)


sns.barplot(data=max_profit, x='City', y= 'Profit')

plt.title('Top 20 highest profit by city')
plt.xticks(rotation=90)
plt.show()

sns.barplot(data=max_sales, x='City', y='Sales')

plt.title('Top 20 highest sales by city')
plt.xticks(rotation=90)
plt.show()

#What are the Top 20 customers by Sales?

custom_sales = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).reset_index()
best_custom= custom_sales.head(20)
print(best_custom)

sns.barplot(data=best_custom, x='Customer Name', y= 'Sales')

plt.title('Best customer by sales')
plt.xticks(rotation=90)
plt.show()

#The Pareto Principle, also known as the 80/20 rule, is a concept derived from the work of Italian economist Vilfredo Pareto. It states that roughly 80% of the effects come from 20% of the causes. For instance, identifying the top 20% of products that generate 80% of sales or the top 20% of customers that contribute to 80% of profit can help in prioritizing efforts and resources. This focus can lead to improved efficiency and effectiveness in business strategies. Can we apply Pareto principle to customers and Profit ? (Determine if 20% of the customers contribute to 80% of the profit.)

# Profit by customer, sorted from highest to lowest
customer_profit = df.groupby("Customer Name")["Profit"].sum().sort_values(ascending=False)

# Convert to DataFrame
pareto = customer_profit.reset_index()
pareto.columns = ["Customer Name", "Profit"]

# Cumulative profit and percentages
pareto["Cumulative Profit"] = pareto["Profit"].cumsum()
pareto["Cumulative Profit %"] = pareto["Cumulative Profit"] / pareto["Profit"].sum() * 100
pareto["Customer %"] = (pareto.index + 1) / len(pareto) * 100

# Plot Pareto curve
plt.figure(figsize=(10, 6))
plt.plot(pareto["Customer %"], pareto["Cumulative Profit %"], marker="o")
plt.axhline(80, color="red", linestyle="--", label="80% Profit")
plt.axvline(20, color="green", linestyle="--", label="20% Customers")

plt.title("Pareto Analysis: Customers vs Profit")
plt.xlabel("Cumulative % of Customers")
plt.ylabel("Cumulative % of Profit")
plt.legend()
plt.grid(True)
plt.show()

# Numeric check
top_20_index = int(0.2 * len(pareto))
top_20_profit_percent = pareto.iloc[:top_20_index]["Profit"].sum() / pareto["Profit"].sum() * 100

#Plot the Cumulative curve in Sales by Customers. Can we apply Pareto principle to customers and Sales ?

# Total sales by customer (sorted)
customer_sales = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)

#Convert to DataFrame
pareto_sales = customer_sales.reset_index()
pareto_sales.columns = ["Customer Name", "Sales"]

#Compute cumulative sales
pareto_sales["Cumulative Sales"] = pareto_sales["Sales"].cumsum()
pareto_sales["Cumulative Sales %"] = pareto_sales["Cumulative Sales"] / pareto_sales["Sales"].sum() * 100

# Compute customer percentage
pareto_sales["Customer %"] = (pareto_sales.index + 1) / len(pareto_sales) * 100

# Plot Pareto curve
plt.figure(figsize=(10, 6))

plt.plot(pareto_sales["Customer %"], pareto_sales["Cumulative Sales %"], marker="o")

# Reference lines
plt.axhline(80, color="red", linestyle="--", label="80% Sales")
plt.axvline(20, color="green", linestyle="--", label="20% Customers")

plt.title("Pareto Analysis: Customers vs Sales")
plt.xlabel("Cumulative % of Customers")
plt.ylabel("Cumulative % of Sales")

plt.legend()
plt.grid(True)
plt.show()

# Numeric check
top_20_index = int(0.2 * len(pareto_sales))
top_20_sales_percent = pareto_sales.iloc[:top_20_index]["Sales"].sum() / pareto_sales["Sales"].sum() * 100


#Based on the analysis, make decisions on which states and cities to prioritize for marketing strategies.

""" States: Prioritize high-performing states like California and New York (high sales and profit), while monitoring states like Texas or Pennsylvania if they show lower profitability.

Cities: Focus on top cities such as New York City, Los Angeles, and San Francisco for strong returns, while optimizing profitability in cities like Philadelphia or Houston if margins are lower.

Je préfère cette réponse """