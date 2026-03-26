import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import mplfinance as mpf

#Initial Data Exploration

#Load data
df = pd.read_csv("AAPL.csv")

# Inspect
print(df.head())
print(df.info())
print(df.isnull().sum())

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Sort by date
df = df.sort_values("Date").reset_index(drop=True)

#Set date as index
df = df.set_index("Date")
print(df.head())

print("Start date:", df.index.min())
print("End date:", df.index.max())
print("Number of rows:", len(df))

# Check spacing between dates
print(df.index.to_series().diff().value_counts().head())

#Data Visualization

#Closing price over time
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Close"])
plt.title("Apple Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.tight_layout()
plt.show()

#Trading volume over time
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Volume"])
plt.title("Apple Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.tight_layout()
plt.show()

#High and low prices
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["High"], label="High")
plt.plot(df.index, df["Low"], label="Low")
plt.title("Apple High and Low Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.show()

#Candlestick chart
#candles = df[["Open", "High", "Low", "Close", "Volume"]].copy()
#mpf.plot(candles.tail(200), type="candle", volume=True, style="yahoo", figsize=(12, 8))

#Statistical Analysis

#Summary statistics
summary_stats = df[["Open", "High", "Low", "Close", "Adj Close", "Volume"]].agg(
    ["mean", "median", "std", "min", "max"]
)
print(summary_stats)

#Daily returns
df["Daily_Return"] = df["Close"].pct_change()
print(df["Daily_Return"].describe())

# moving average
df["MA_20"] = df["Close"].rolling(window=20).mean()
df["MA_50"] = df["Close"].rolling(window=50).mean()

plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Close"], label="Close")
plt.plot(df.index, df["MA_20"], label="20-day MA")
plt.plot(df.index, df["MA_50"], label="50-day MA")
plt.title("Apple Closing Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.show()

close_array = df["Close"].dropna().to_numpy()
ma_20_np = np.convolve(close_array, np.ones(20)/20, mode="valid")

print(ma_20_np[:5])

#Hypothesis Testing

#T-test comparing average closing prices across years
df["Year"] = df.index.year

close_2021 = df[df["Year"] == 2021]["Close"].dropna()
close_2022 = df[df["Year"] == 2022]["Close"].dropna()

t_stat, p_value = stats.ttest_ind(close_2021, close_2022, equal_var=False)

print("T-statistic:", t_stat)
print("P-value:", p_value)

#Test daily returns for normality
returns = df["Daily_Return"].dropna()

# Shapiro-Wilk works best on smaller samples, so sample if needed
sample_returns = returns.sample(min(5000, len(returns)), random_state=42)

shapiro_stat, shapiro_p = stats.shapiro(sample_returns)
print("Shapiro-Wilk p-value:", shapiro_p)

plt.figure(figsize=(10, 5))
plt.hist(returns, bins=100)
plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#Q-Q plot

plt.figure(figsize=(6, 6))
stats.probplot(returns, dist="norm", plot=plt)
plt.title("Q-Q Plot of Daily Returns")
plt.tight_layout()
plt.show()

#Summary

""" This project analyzes Apple stock data using Pandas, NumPy, Matplotlib, and SciPy. It explores price trends, trading volume, and daily returns through visualization and statistical analysis. Moving averages highlight long-term patterns, while hypothesis testing and normality tests provide insight into the behavior of stock returns. Overall, the project demonstrates how data analysis techniques can be applied to financial time series data. """