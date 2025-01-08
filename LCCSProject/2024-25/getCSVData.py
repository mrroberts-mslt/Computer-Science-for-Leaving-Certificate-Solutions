import pandas as pd

# GitHub “raw” URL for the CSV file
url = "https://raw.githubusercontent.com/owid/monkeypox/main/owid-monkeypox-data.csv"

# Read the CSV directly into a pandas DataFrame
df = pd.read_csv(url)

# Display the first few rows
print(df.head())
