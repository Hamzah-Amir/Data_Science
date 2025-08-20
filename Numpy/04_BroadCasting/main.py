# Numpy provides broadcating to apply mathmatical operations on a dataset without loops 
# It is faster then normal python loops

# Consider we have list of price of products and we are giving 10% off for one day

# Calculating discount and adding in final prices using tradiitional way
prices = [100,150,190,165,355,670]
discount = 10
final_prices = []

for price in prices:
    discounted_price = int(price - (price * discount / 100))
    final_prices.append(discounted_price)
print(final_prices)

# We can do same thing using broadcasting in numpy in an efficient way

import numpy as np
prices = np.array([100,150,190,165,355,670])
discount = 10
final_prices = prices - (prices * discount / 100)
final_prices = final_prices.astype(int)
print(final_prices)