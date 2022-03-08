
# Merge on the 'uid' field
uid_combined_data = app_purchases.merge(customer_data, how='inner', on=['uid'])

# Examine the results
print(uid_combined_data.head())
print(len(uid_combined_data))


# Merge on the 'uid' and 'date' field
uid_date_combined_data = app_purchases.merge(customer_data, on=['uid', 'date'], how='inner')

# Examine the results
print(uid_date_combined_data.head())
print(len(uid_date_combined_data))