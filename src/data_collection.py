"""
data_collection.py

This module is responsible for loading the fake news dataset.
"""

import pandas as pd


def load_dataset(file_path):
    """
    Load dataset from a CSV file.
    """
    try:
        dataset = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return dataset
    except FileNotFoundError:
        print("Dataset file not found.")
        return None


if __name__ == "__main__":
    print("Data Collection Module")