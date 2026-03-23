import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. Data Preparation:
# Define cities and months
cities = [
    "New York", "London", "Tokyo", "Paris", "Tel Aviv",
    "Sydney", "Brussels", "Toronto", "Jerusalem", "Amsterdam"
]

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# Generate synthetic temperature data: 10 cities x 12 months
temperature_data = np.random.uniform(-5, 35, size=(10, 12))

# Convert to DataFrame
df = pd.DataFrame(temperature_data, index=cities, columns=months)

print(df)
print()

#2. Data Analysis:
# Calculate annual average temperature for each city
annual_avg = df.mean(axis=1)

print("Annual average temperature for each city:")
print(annual_avg)

# Find hottest and coldest city on average
hottest_city = annual_avg.idxmax()
coldest_city = annual_avg.idxmin()

print("\nCity with highest average temperature:", hottest_city)
print("With an average temperature of:", annual_avg.max())

print("\nCity with lowest average temperature:", coldest_city)
print("With an average temperature of:", annual_avg.min())
print()

df["Annual Average"] = annual_avg
print(df)
print()

#3. Data Visualization:
plt.figure(figsize=(12, 6))

for city in df.index:
    plt.plot(months, df.loc[city, months], marker='o', label=city)

plt.title("Average Monthly Temperatures Across 10 Cities")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend(bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45)
plt.show()


