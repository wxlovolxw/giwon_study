import pandas as pd

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv('airline_bumping', delimiter = ',')

# Take a look at the DataFrame
print(airline_bumping.head())

airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)