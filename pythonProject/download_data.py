import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

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
monthly_discount_rate = (1 + annual_discount_rate) ** (1 / 12) - 1

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
