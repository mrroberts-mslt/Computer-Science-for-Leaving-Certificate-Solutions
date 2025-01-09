import pandas as pd

# Load the dataset
DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/owid-covid-data.csv"
df = pd.read_csv(DATA_URL)
# Filter data for the United States
us_df = df[df['iso_code'] == 'USA']

# Select relevant columns
columns_of_interest = ['date', 'new_cases', 'new_deaths', 'total_cases', 'total_deaths', 'people_vaccinated']
us_df = us_df[columns_of_interest]

# Clean data
us_df = us_df.dropna()  # Drop rows with missing values
us_df['date'] = pd.to_datetime(us_df['date'])  # Convert 'date' to datetime
us_df.to_csv('cleaned_us_covid_data.csv', index=False)

