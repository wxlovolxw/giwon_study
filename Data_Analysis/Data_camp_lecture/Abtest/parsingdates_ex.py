
import pandas as pd

date_data_one = ['Saturday January 27, 2017', 'Saturday December 2, 2017']
date_data_two = ['2017-01-01', '2016-05-03']
date_data_three = ['08/17/1978', '01/07/1976']
date_date_four = ['2016 March 01 01:56', '2016 January 4 02:16']

# Provide the correct format for the date

# Provide the correct format for the following date: Saturday January 27, 2017
date_data_one = pd.to_datetime(date_data_one, format = "%A %B %d, %Y")
print(date_data_one)

# Provide the correct format for the following date: 2017-08-01
date_data_two = pd.to_datetime(date_data_two, format = "%Y-%m-%d")

# Provide the correct format for the following date: 08/17/1978
date_data_three = pd.to_datetime(date_data_three, format = "%m/%d/%Y")

# Provide the correct format for the following date: 2016 March 01 01:56
date_data_four = pd.to_datetime(date_date_four, format = "%Y %B %d %H:%M")