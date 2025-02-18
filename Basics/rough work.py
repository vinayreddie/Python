a,b,c=7,5,4

single,doublequote='peter',"john"
"""concat"""
concat=single+' '+doublequote
co=single.upper()
d=b%a
print(a,c)
print(d)
a = [2] * 5  # Creates a list with 5 zeros
print(a)  # Output: [0, 0, 0, 0, 0]
print(single,doublequote,concat,co)

import numpy as np

# Historical returns in percentage
historical_returns = np.array([7.00, 8.00, 10.00, 13.56, 14.00]) / 100  # Convert to decimal

# Initial stock price
initial_price = 240

# Calculate stock price over 5 years
prices = [initial_price]
for r in historical_returns:
    new_price = prices[-1] * (1 + r)
    prices.append(new_price)

# Output the stock prices for each year
for year, price in enumerate(prices):
    print(f"Year {year}: ${price:.2f}")
    
print(prices)


Company_A_Fundamentals = {
    'Market_Cap': 250,
    'Share_Price': 148.34,
    'outstanding_shares': (250 * 1e6) / 148.34
}

# Add a new key and delete the old one
Company_A_Fundamentals['Market Capitalization'] = Company_A_Fundamentals.pop('Market_Cap')

# Print updated dictionary
print(Company_A_Fundamentals)

Historical_Returns = [1, 2, 3, 4, 5]

for i in Historical_Returns:
    print(i)


message = 'Hello'
for i in message:
  print(i)

for i in range(20,200,20):
    print(i)

counter = 5
while counter > 0:
 print("Counter = ",counter) 
 counter = counter -1