"""
Clinical Data Utilities
Author: Maria Triantafyllia Patentalaki
"""

import pandas as pd


def load_data(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path)


def dataset_summary(df):
    """
    Print basic information about the dataset.
    """
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn names:")
    print(df.columns.tolist())