import pandas as pd
from data_preparation import load_and_clean_data

def analyze_data(data):
    """
    Perform basic data analysis.
    Args:
        data (DataFrame): The cleaned dataset.
    Returns:
        None
    """
    # Example: Display basic statistics
    print(data.describe())
    # Add more analysis as needed

if __name__ == "__main__":
    filepath = 'C:/Users/octav/Downloads/Marketing Analyst Project_Insights Analysis - Metrics Statistic Modeling results.csv'
    data = load_and_clean_data(filepath)
    analyze_data(data)
