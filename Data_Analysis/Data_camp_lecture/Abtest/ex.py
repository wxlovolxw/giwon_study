from datetime import datetime, timedelta
import pandas as pd

current_date = pd.to_datetime('2020-08-03')
max_lapse_date = current_date - timedelta(days=7)

print(max_lapse_date > pd.to_datetime('2020-07-20'))