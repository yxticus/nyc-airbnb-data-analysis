import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/nyc-tlc/trip-data/master/green_tripdata_2020-01.csv"
df = pd.read_csv(url)

# Basic cleaning
df = df[['trip_distance', 'fare_amount']].dropna()

# Summary stats
print("Summary Statistics:")
print(df.describe())

# Simple visualization
plt.scatter(df['trip_distance'], df['fare_amount'], alpha=0.3)
plt.xlabel("Trip Distance")
plt.ylabel("Fare Amount")
plt.title("NYC Trip Distance vs Fare")
plt.show()
