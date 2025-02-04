from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Prevents GUI error
import io
import base64

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

def generate_plot():
    plt.figure(figsize=(10, 5))

    # Convert columns to numeric
    monthly_data["total_cases"] = pd.to_numeric(monthly_data["total_cases"], errors="coerce")
    monthly_data["total_deaths"] = pd.to_numeric(monthly_data["total_deaths"], errors="coerce")

    # Ensure Year-Month is a string
    monthly_data["Year-Month"] = monthly_data["Year-Month"].astype(str)

    # Plot Spain and UK separately
    spain = monthly_data[monthly_data["location"] == "Spain"]
    uk = monthly_data[monthly_data["location"] == "United Kingdom"]

    plt.plot(spain["Year-Month"], spain["total_cases"], marker='o', label="Spain", color="blue")
    plt.plot(uk["Year-Month"], uk["total_cases"], marker='s', label="United Kingdom", color="red")

    plt.xticks(rotation=45)
    plt.xlabel("Year-Month")
    plt.ylabel("Total Cases")
    plt.title("Monthly Monkeypox Cases in Spain & UK")
    plt.legend()

    # Save plot to a bytes buffer
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches="tight")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url


@app.route('/')
def home():
    """Render homepage with stats and graph"""
    max_cases = monthly_data['total_cases'].max()
    min_cases = monthly_data['total_cases'].min()
    total_cases = monthly_data['total_cases'].sum()
    average_cases = round(total_cases / len(monthly_data), 2)

    max_deaths = monthly_data['total_deaths'].max()
    min_deaths = monthly_data['total_deaths'].min()
    total_deaths = monthly_data['total_deaths'].sum()
    average_deaths = round(total_deaths / len(monthly_data), 2)

    graph = generate_plot()

    return render_template('index.html', max_cases=max_cases, min_cases=min_cases, total_cases=total_cases,
                           average_cases=average_cases, max_deaths=max_deaths, min_deaths=min_deaths,
                           total_deaths=total_deaths, average_deaths=average_deaths, graph=graph)


@app.route('/api/data')
def get_data():
    """Return JSON data"""
    return jsonify({
        "max_cases": monthly_data['total_cases'].max(),
        "min_cases": monthly_data['total_cases'].min(),
        "total_cases": monthly_data['total_cases'].sum(),
        "average_cases": round(monthly_data['total_cases'].sum() / len(monthly_data), 2),
        "max_deaths": monthly_data['total_deaths'].max(),
        "min_deaths": monthly_data['total_deaths'].min(),
        "total_deaths": monthly_data['total_deaths'].sum(),
        "average_deaths": round(monthly_data['total_deaths'].sum() / len(monthly_data), 2),
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change port if necessary

