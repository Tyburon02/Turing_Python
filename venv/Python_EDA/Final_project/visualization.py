import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd  # Make sure to import pandas
from data_preparation import load_and_clean_data


def create_visualizations(data):
    """
    Create visualizations of the dataset.
    Args:
        data (DataFrame): The cleaned dataset.
    """
    #Convert the'hour_of_day' to numerical hour format 'HH:MM:SS AM/PM'.
    data['hour_of_day'] = pd.to_datetime(data['hour_of_day'], format='%I:%M:%S %p').dt.hour

    # Example: Line plot for total revenue by hour of day
    plt.figure()
    sns.lineplot(data=data, x='hour_of_day', y='total_revenue')
    plt.title('Total Revenue by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Total Revenue')
    plt.show()
    
    # Example: Bar plot for total conversions by weekday
    plt.figure()
    sns.barplot(data=data, x='weekday_name', y='total_conversions')
    plt.title('Total Conversions by Weekday')
    plt.xlabel('Weekday')
    plt.ylabel('Total Conversions')
    plt.show()

    # Total Revenue by Weekday
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x='weekday_name', y='total_revenue', ci=None)
    plt.title('Total Revenue by Weekday')
    plt.xlabel('Weekday')
    plt.ylabel('Total Revenue')
    plt.show()

    # Total Visits by Hour of Day
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='hour_of_day', y='total_visits')
    plt.title('Total Visits by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Total Visits')
    plt.show()

if __name__ == "__main__":
    filepath = 'C:/Users/octav/Downloads/Marketing Analyst Project_Insights Analysis - Metrics Statistic Modeling results.csv'
    data = load_and_clean_data(filepath)
    create_visualizations(data)



