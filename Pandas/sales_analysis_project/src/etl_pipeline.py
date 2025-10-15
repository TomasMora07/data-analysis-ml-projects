"""
ETL PIPELINE MODULE
-------------------
Contains reusable functions for extracting, transforming,
and loading sales data from multiple sources.
"""

import pandas as pd
import os


# EXTRACT

def extract_data(file_path_1, file_path_2):
    """
    Loads two CSV datasets and combines them into a single DataFrame.
    Adds a store identifier for traceability.
    """
    df1 = pd.read_csv(file_path_1)
    df2 = pd.read_csv(file_path_2)

    # Add source label
    df1['store'] = 'Store_1'
    df2['store'] = 'Store_2'

    # Combine both datasets
    df = pd.concat([df1, df2], ignore_index=True)
    print(f"Data extracted: {df.shape[0]} rows from both stores")
    return df

# TRANSFORM

def transform_data(df):
    """
    Cleans and standardizes the dataset:
    - Normalizes column names
    - Fixes data types
    - Recalculates total sales
    - Removes invalid values
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Convert columns
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')
    df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce')

    # Calculate total sales and filter valid rows
    df['total_venta'] = df['cantidad'] * df['precio_unitario']
    df = df[(df['cantidad'] > 0) & (df['precio_unitario'] > 0)]

    print("Data transformed successfully.")
    return df

# LOAD

def load_data(df, output_path="../data/processed/"):
    """
    Saves the cleaned dataset to the processed folder as 'merged_sales.csv'.
    """
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, "merged_sales.csv")
    df.to_csv(output_file, index=False)
    print(f"Data loaded and saved to: {output_file}")
    return output_file
