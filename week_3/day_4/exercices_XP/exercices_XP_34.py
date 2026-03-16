import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


#exercice 1
""" Data visualization is important because it helps analysts understand patterns, trends, and relationships in data. It makes complex datasets easier to interpret and helps communicate insights clearly to others.

A line graph is used to display how data changes over time or across a continuous variable. It helps identify trends, patterns, and rates of change in the data. """

#exercice 2

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [72, 74, 76, 80, 82, 78, 75]

plt.plot(days, temperatures)
plt.title("temperature variation over a week")
plt.xlabel("Day")
plt.ylabel("Temperature (F)")
plt.show()

#exercice 3
months = ['January', 'February', 'March', 'April', 'May']
sales = [5000, 5500, 6200, 7000, 7500]

plt.bar(months, sales)
plt.title('Monthly Sales Report')
plt.xlabel('Month')
plt.ylabel('Sales Amount ($)')
plt.show()

#exercice 4

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "StudentMentalhealth.csv")

df = pd.read_csv(file_path)

plt.figure(figsize=(10,6))

sns.histplot(data=df, x='What is your CGPA?', bins=20, color='purple')

plt.title('distribution of CGPA', fontsize=16, fontweight='bold')
plt.xlabel('CGPA', fontsize=12)
plt.ylabel('Number of students', fontsize=20)
plt.show()

#exercice 5

# Convert anxiety answers to numeric values
df["Anxiety_numeric"] = df["Do you have Anxiety?"].map({"Yes": 1, "No": 0})

plt.figure(figsize=(12,6))

sns.barplot(
    data=df,
    x="Choose your gender",
    y="Anxiety_numeric",
    hue="Choose your gender",
    palette={"Male": "blue", "Female": "pink"},
    legend=False
)

plt.title("Anxiety Across Genders", fontsize=16, fontweight="bold")
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Anxiety", fontsize=12)
plt.show()

#exercice 6

# Convert panic attack responses to numeric values
df["panic_numeric"] = df["Do you have Panic attack?"].map({"Yes": 1, "No": 0})

plt.figure(figsize=(12, 6))

sns.scatterplot(data=df, x='Age', y='panic_numeric')

plt.title('Panic attack according to age', fontsize=16, fontweight='bold')
plt.xlabel('Age')
plt.ylabel('panic attack')
plt.show()

