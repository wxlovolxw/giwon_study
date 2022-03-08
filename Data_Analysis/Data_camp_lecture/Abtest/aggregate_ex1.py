
# Calculate the mean purchase price
purchase_price_mean = purchase_data.price.agg('mean')
# Examine the output
print(purchase_price_mean)

# Calculate the mean and median purchase price
purchase_price_summary = purchase_data.price.agg(['mean','median'])
# Examine the output
print(purchase_price_summary)

# Calculate the mean and median of price and age
purchase_summary = purchase_data.agg({'price':['mean','median'],'age':['mean','median']})
# Examine the output
print(purchase_summary)