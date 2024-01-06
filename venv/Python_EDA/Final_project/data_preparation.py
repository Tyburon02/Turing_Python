import pandas as pd

def load_and_clean_data(filepath):
    """
    Load and clean the dataset.
    Args:
        filepath (str): Path to the CSV file.
    Returns:
        DataFrame: Cleaned DataFrame.
    """
    data = pd.read_csv(filepath)
    data.fillna(0, inplace=True)  # Replace missing values with 0
    # Add more data cleaning steps as needed
    return data

if __name__ == "__main__":
    filepath = 'C:/Users/octav/Downloads/Marketing Analyst Project_Insights Analysis - Metrics Statistic Modeling results.csv'
    data = load_and_clean_data(filepath)
    print(data.head())

