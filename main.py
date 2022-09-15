# INF601 - Advanced Programming in Python
# Jason Zeller
# Mini Project 1


import yfinance as yf

data = yf.download("MSFT", start="2022-08-30", end="2022-09-14")

msftPrices = []

for price in data['Adj Close']:
    msftPrices.append(price)

print(msftPrices)