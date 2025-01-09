import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from flask import Flask, render_template, request

# Configure Matplotlib to use a non-GUI backend
matplotlib.use('Agg')

app = Flask(__name__)

# Load and prepare the data
DATA_URL = "cleaned_us_covid_data.csv"

df = pd.read_csv(DATA_URL)
df['date'] = pd.to_datetime(df['date'])

@app.route("/", methods=["GET", "POST"])
def index():
    start_date = df['date'].min()
    end_date = df['date'].max()

    # Handle date range selection
    if request.method == "POST":
        start_date = request.form.get("start_date", start_date)
        end_date = request.form.get("end_date", end_date)

    # Filter data
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    create_graphs(filtered_df)

    return render_template("index.html", start_date=start_date, end_date=end_date)

def create_graphs(data):
    # Generate Line Chart
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['new_cases'], label="New Cases", color="blue")
    plt.title("Daily New COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.grid(True)
    plt.legend()
    plt.savefig("static/graphs/line_chart.png")
    plt.close()

    # Generate Bar Chart
    plt.figure(figsize=(10, 6))
    plt.bar(data['date'], data['people_vaccinated'], color="skyblue")
    plt.title("Total People Vaccinated Over Time")
    plt.xlabel("Date")
    plt.ylabel("People Vaccinated")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/graphs/bar_chart.png")
    plt.close()

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0", port=8000)
