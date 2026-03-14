import scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm, binom


# Exercise 1

print("SciPy version:", scipy.__version__)

# Exercise 2

data = [12, 15, 13, 12, 18, 20, 22, 21]

mean_value = stats.tmean(data)
median_value = np.median(data)
variance_value = stats.tvar(data)
std_dev_value = stats.tstd(data)

print("Mean:", mean_value)
print("Median:", median_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)

# Exercise 3

mean = 50
std_dev = 10

x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 500)
y = norm.pdf(x, mean, std_dev)

plt.plot(x, y)
plt.title("Normal Distribution (mean=50, std=10)")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.grid(True)
plt.show()

# Exercise 4

np.random.seed(42)

data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)

t_stat, p_value = stats.ttest_ind(data1, data2)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("The difference between the two groups is statistically significant.")
else:
    print("The difference between the two groups is NOT statistically significant.")

# Exercise 5

house_sizes = np.array([50, 70, 80, 100, 120])
house_prices = np.array([150000, 200000, 210000, 250000, 280000])

result = stats.linregress(house_sizes, house_prices)

slope = result.slope
intercept = result.intercept
predicted_price_90 = slope * 90 + intercept

print("Slope:", slope)
print("Intercept:", intercept)
print("Predicted price for 90 square meters:", predicted_price_90)
print("R-squared:", result.rvalue ** 2)

# Exercise 6

fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]

f_stat, p_value = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

print("F-value:", f_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("The fertilizers have significantly different effects on plant growth.")
else:
    print("There is no statistically significant difference between the fertilizers.")

# Exercise 7

probability = binom.pmf(5, 10, 0.5)
print("Probability of getting exactly 5 heads:", probability)

# Exercise 8

df = pd.DataFrame({
    'age': [23, 25, 30, 35, 40],
    'income': [35000, 40000, 50000, 60000, 70000]
})

pearson_corr, pearson_p = stats.pearsonr(df['age'], df['income'])
spearman_corr, spearman_p = stats.spearmanr(df['age'], df['income'])

print("Pearson correlation:", pearson_corr)
print("Pearson p-value:", pearson_p)
print("Spearman correlation:", spearman_corr)
print("Spearman p-value:", spearman_p)