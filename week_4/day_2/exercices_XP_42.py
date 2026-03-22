import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
print('ex 1')

matrix = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

det = np.linalg.det(matrix)
inv = np.linalg.inv(matrix)

print("Matrix:")
print(matrix)

print("\nDeterminant:")
print(det)

print("\nInverse:")
print(inv)
print()

#2
print('ex2')

data = np.random.rand(50)

mean_val = np.mean(data)
median_val = np.median(data)
std_val = np.std(data)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard deviation:", std_val)
print()

#3
print('ex3')
dates = np.arange('2023-01-01', '2023-02-01', dtype='datetime64[D]')
print("Original dates:")
print(dates)

formatted_dates = [str(date).replace('-', '/') for date in dates]
print("\nFormatted dates:")
print(formatted_dates)
print()

#4
print('ex4')
data = np.random.rand(5, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

print("DataFrame:")
print(df)

print("\nRows where column A > 0.5:")
print(df[df['A'] > 0.5])

print("\nColumn sums:")
print(df.sum())

print("\nColumn averages:")
print(df.mean())
print()

#5
print('ex5')
import numpy as np

# Images in NumPy are represented as arrays where each value corresponds to a pixel intensity (0 = black, 255 = white)

image = np.array([
    [0, 50, 100, 150, 200],
    [25, 75, 125, 175, 225],
    [0, 50, 100, 150, 200],
    [25, 75, 125, 175, 225],
    [0, 50, 100, 150, 200]
])
print(image)
print()

#6
print('ex6')
# Productivity scores of employees before the training program
productivity_before = np.random.normal(loc=50, scale=10, size=30)

# Productivity scores of the same employees after the training program
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

mean_before = np.mean(productivity_before)
mean_after = np.mean(productivity_after)
difference = productivity_after - productivity_before
mean_difference = np.mean(difference)

print("Mean productivity before training:", mean_before)
print("Mean productivity after training:", mean_after)
print("Mean improvement:", mean_difference)
print()

#7
print('ex7')
arr1 = np.array([5, 8, 2, 7, 9])
arr2 = np.array([3, 8, 4, 6, 10])

comparison = arr1 > arr2

print(comparison)
print()

#8
print('ex8')
dates = np.arange('2023-01', '2024-01', dtype='datetime64[D]')

jan_mar = dates[(dates >= np.datetime64('2023-01-01')) & (dates < np.datetime64('2023-04-01'))]
apr_jun = dates[(dates >= np.datetime64('2023-04-01')) & (dates < np.datetime64('2023-07-01'))]
jul_sep = dates[(dates >= np.datetime64('2023-07-01')) & (dates < np.datetime64('2023-10-01'))]
oct_dec = dates[(dates >= np.datetime64('2023-10-01')) & (dates < np.datetime64('2024-01-01'))]

print("January to March:")
print(jan_mar)

print("\nApril to June:")
print(apr_jun)

print("\nJuly to September:")
print(jul_sep)

print("\nOctober to December:")
print(oct_dec)
print()

#9
print('ex9')
# NumPy array to DataFrame
arr = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(arr, columns=['Col1', 'Col2'])

print("DataFrame:")
print(df)

# DataFrame back to NumPy array
np_arr = df.to_numpy()

print("\nConverted back to NumPy array:")
print(np_arr)
print()

#10
print('ex10')
data = np.random.rand(10)

plt.plot(data)
plt.title("Line Graph of Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()