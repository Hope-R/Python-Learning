stock_prices = [("Apple",100),("Google",101),("Microsoft",99)]
for x in stock_prices:
    print(x)

for ticker,price in stock_prices:
    print(price*.1)