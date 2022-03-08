import pandas as pd
import matplotlib.pyplot as plt

avocados_2016 = pd.read_csv('avocados_2016.csv', delimiter =',')

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())