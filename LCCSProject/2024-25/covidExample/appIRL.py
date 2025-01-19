import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from flask import Flask, render_template, request

# Configure Matplotlib to use a non-GUI backend
matplotlib.use('Agg')

app = Flask(__name__)

# Load and prepare the data
DATA_URL = "owid-covid-data.csv"
df = pd.read_csv(DATA_URL)
irl_df = df[df['iso_code'] == 'IRL']
irl_df['date'] = pd.to_datetime(irl_df['date'])
columns_of_interest = ['date', 'new_cases', 'new_deaths', 'total_cases', 'total_deaths', 'people_vaccinated']
irl_df = irl_df[columns_of_interest].dropna()

@app.route("/", methods=["GET", "POST"])
def index():
    # Default start and end dates
    start_date = irl_df['date'].min()
    end_date = irl_df['date'].max()

    # Handle form submission
    if request.method == "POST":
        start_date = request.form.get("start_date", start_date)
        end_date = request.form.get("end_date", end_date)

    # Filter data based on the selected date range
    filtered_df = irl_df[(irl_df['date'] >= start_date) & (irl_df['date'] <= end_date)]

    # Generate graphs
    generate_line_chart(filtered_df)
    generate_bar_chart(filtered_df)

    return render_template("index.html", start_date=start_date, end_date=end_date)

def generate_line_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['new_cases'], label="New Cases")
    plt.title("Daily New COVID-19 Cases in Ireland")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    graph_path = os.path.join("static", "graphs", "line_chart.png")
    plt.savefig(graph_path)
    plt.close()

def generate_bar_chart(data):
    plt.figure(figsize=(10, 6))
    plt.bar(data['date'], data['people_vaccinated'], color="skyblue")
    plt.title("Total People Vaccinated Over Time in Ireland")
    plt.xlabel("Date")
    plt.ylabel("People Vaccinated")
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph_path = os.path.join("static", "graphs", "bar_chart.png")
    plt.savefig(graph_path)
    plt.close()

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0", port=8000)

