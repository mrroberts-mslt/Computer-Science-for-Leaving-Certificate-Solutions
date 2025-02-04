from flask import Flask, render_template, jsonify
import pandas as pd
import csv

app = Flask(__name__)

# Load and preprocess data
DATA_URL = "https://raw.githubusercontent.com/owid/monkeypox/refs/heads/main/owid-monkeypox-data.csv"
df = pd.read_csv(DATA_URL)

# Filter data for Spain and the UK
spain_df = df[df['iso_code'] == 'ESP']
uk_df = df[df['iso_code'] == 'GBR']

# Select relevant columns
columns_of_interest = ['location', 'total_cases', 'total_deaths', 'date']
uk_df = uk_df[columns_of_interest]
spain_df = spain_df[columns_of_interest]

# Clean the data
spain_df = spain_df.dropna()
uk_df = uk_df.dropna()

# Combine datasets
combined_df = pd.concat([spain_df, uk_df])

# Convert date to Year-Month format
combined_df['date'] = pd.to_datetime(combined_df['date'])
combined_df['Year-Month'] = combined_df['date'].dt.to_period('M')

# Aggregate data by month
monthly_data = combined_df.groupby(['location', 'Year-Month']).sum().reset_index()

# Save cleaned data
monthly_data.to_csv("monthly_cleaned_data.csv", index=False)
combined_df.to_csv("cleaned_up_data.csv", index=False)

# Read processed CSV data for API
with open("monthly_cleaned_data.csv", "r") as file:
    reader = csv.DictReader(file)
    death_data = [float(row['total_deaths']) for row in reader if row['total_deaths'].replace('.', '', 1).isdigit()]

with open("monthly_cleaned_data.csv", "r") as file:
    reader = csv.DictReader(file)
    case_data = [float(row['total_cases']) for row in reader if row['total_cases'].replace('.', '', 1).isdigit()]

# Calculate statistics
max_deaths = max(death_data)
min_deaths = min(death_data)
total_deaths = sum(death_data)
average_deaths = round(total_deaths / len(death_data), 2)

max_cases = max(case_data)
min_cases = min(case_data)
total_cases = sum(case_data)
average_cases = round(total_cases / len(case_data), 2)


@app.route('/')
def home():
    """Render homepage"""
    return render_template('index.html', max_cases=max_cases, min_cases=min_cases, total_cases=total_cases,
                           average_cases=average_cases, max_deaths=max_deaths, min_deaths=min_deaths,
                           total_deaths=total_deaths, average_deaths=average_deaths)


@app.route('/api/data')
def get_data():
    """Return JSON data"""
    return jsonify({
        "max_cases": max_cases,
        "min_cases": min_cases,
        "total_cases": total_cases,
        "average_cases": average_cases,
        "max_deaths": max_deaths,
        "min_deaths": min_deaths,
        "total_deaths": total_deaths,
        "average_deaths": average_deaths
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change port number
