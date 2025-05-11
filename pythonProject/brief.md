Certainly! Let's proceed with the replication of Robert J. Shiller's seminal article, "Do Stock Prices Move Too Much to Be Justified by Subsequent Changes in Dividends?" We'll address the tasks in two parts as outlined.

---

## Part 1: Article Replication

### 1. Summary of the Article and Econometric Model

Objective:
Shiller investigates whether the volatility of stock prices can be justified by subsequent changes in dividends, challenging the Efficient Market Hypothesis (EMH).([Википедия][1])

Key Concepts:

* Efficient Market Hypothesis (EMH): Suggests that stock prices fully reflect all available information, implying that prices should equal the present value of expected future dividends.([Американская Экономическая Ассоциация][2])

* Present Value Model:
  The price of a stock is the discounted sum of expected future dividends:
  $P_t = \sum_{k=1}^{\infty} \frac{E_t[D_{t+k}]}{(1 + r)^k}$
  where $P_t$ is the price at time $t$, $D_{t+k}$ is the dividend at time $t+k$, $E_t$ denotes the expectation based on information at time $t$, and $r$ is the constant discount rate.

Methodology:

* Ex-Post Rational Price:
  Shiller computes the "ex-post rational price" by discounting actual future dividends, assuming perfect foresight:([NBER][3])
  $P_t^* = \sum_{k=1}^{\infty} \frac{D_{t+k}}{(1 + r)^k}$

* Comparison:
  He compares the volatility of actual stock prices $P_t$ with the ex-post rational prices $P_t^*$. If markets are efficient, $P_t$ should not be more volatile than $P_t^*$.

Findings:

* Actual stock prices exhibit greater volatility than can be justified by subsequent changes in dividends.([SSRN][4])

* This excess volatility suggests that factors other than dividends, such as investor psychology, may significantly influence stock prices.

Conclusion:

Shiller's analysis challenges the EMH by demonstrating that stock prices are more volatile than the present value of future dividends would suggest, implying that markets may not always be efficient.([Википедия][1])

### 2. Original Data Used in the Article

Shiller utilized historical data on U.S. stock prices and dividends, primarily focusing on the Standard & Poor's Composite Stock Price Index. The data spans from the late 19th century to the late 20th century.

Data Sources:

* Historical stock price and dividend data were compiled from various sources, including the Cowles Commission and Standard & Poor's.

* Shiller's own dataset, which includes monthly data on stock prices, dividends, and earnings, is publicly available on his Yale University website:

  [Robert Shiller's Online Data](http://www.econ.yale.edu/~shiller/data.htm)

### 3. New Data for Replication

To replicate Shiller's analysis with updated data, we can utilize:

* Yahoo Finance: Provides historical stock prices and dividend data for various indices and companies.

* Standard & Poor's: Offers comprehensive data on the S\&P 500 index, including price and dividend information.

* Robert Shiller's Online Data: Updated datasets are available on his website, which can serve as a benchmark.

### 4. Python Code for Replication

Below is a Python script that replicates Shiller's analysis using the yfinance library to fetch data from Yahoo Finance.


import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol for the S&P 500 index
ticker = '^GSPC'

# Fetch historical data
data = yf.download(ticker, start='1980-01-01', end='2025-01-01', interval='1mo')

# Drop rows with missing values
data = data.dropna()

# Calculate monthly returns
data['Return'] = data['Adj Close'].pct_change()

# Assume a constant annual discount rate of 6%
annual_discount_rate = 0.06
monthly_discount_rate = (1 + annual_discount_rate) ** (1/12) - 1

# Calculate ex-post rational price
# For each point in time, calculate the present value of future dividends
# Since dividend data is not directly available from yfinance for indices, we'll simulate it
# For demonstration purposes, assume a constant dividend yield of 2%
dividend_yield = 0.02
data['Dividend'] = data['Adj Close'] * dividend_yield / 12  # Monthly dividend

# Calculate ex-post rational price
ex_post_prices = []
for i in range(len(data)):
    future_dividends = data['Dividend'].iloc[i:]
    discounts = [(1 + monthly_discount_rate) ** n for n in range(1, len(future_dividends) + 1)]
    pv = np.sum(future_dividends.values / discounts)
    ex_post_prices.append(pv)

data['ExPostPrice'] = ex_post_prices

# Plot actual vs. ex-post rational prices
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Adj Close'], label='Actual Price')
plt.plot(data.index, data['ExPostPrice'], label='Ex-Post Rational Price')
plt.title('Actual vs. Ex-Post Rational Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Calculate standard deviations
actual_std = data['Adj Close'].std()
ex_post_std = data['ExPostPrice'].std()

print(f"Standard Deviation of Actual Prices: {actual_std}")
print(f"Standard Deviation of Ex-Post Rational Prices: {ex_post_std}")
...

Note:

* This script assumes a constant dividend yield due to the lack of direct dividend data for indices from Yahoo Finance. For a more accurate analysis, consider using actual dividend data from reliable sources.

* The script calculates the ex-post rational price by discounting future simulated dividends.([NBER][3])

---

## Part 2: Research Task

### 1. Research Task, Relevance, and Hypotheses

Research Task:

Investigate whether the volatility of stock prices in emerging markets, such as Russia, can be justified by subsequent changes in dividends, replicating Shiller's methodology.

Relevance:

Emerging markets often exhibit higher volatility due to economic and political uncertainties. Understanding whether this volatility aligns with fundamental factors like dividends is crucial for investors and policymakers.

Hypotheses:

* Null Hypothesis (H0): Stock price volatility in emerging markets is justified by subsequent changes in dividends.

* Alternative Hypothesis (H1): Stock price volatility in emerging markets exceeds what can be justified by subsequent changes in dividends.

### 2. Data Sources

To conduct this analysis, we'll utilize:

* RLMS-HSE: The Russia Longitudinal Monitoring Survey provides comprehensive data on households, which can be used to infer economic conditions.

* Rosstat: The Russian Federal State Statistics Service offers macroeconomic indicators, including corporate profits and dividends.

* World Bank: Provides global economic data, including stock market indices and financial indicators for Russia.

* Yahoo Finance: For historical stock prices and dividend data of Russian companies or indices.

### 3. Descriptive Analysis

Steps:
...