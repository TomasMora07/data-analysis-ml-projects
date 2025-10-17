"""
UTILS MODULE
------------
Contains validation, reporting, and visualization utilities
for the sales analysis project.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os



# VALIDATION

def validate_data(df):
    """
    Prints data quality checks such as:
    - Missing values
    - Duplicate rows
    - Invalid numeric values
    """
    print("Missing values:\n", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())
    print("Invalid values:", ((df['cantidad'] <= 0) | (df['precio_unitario'] <= 0)).sum())


# REPORTING

def generate_sales_report(df, output_folder="../outputs/"):
    """
    Generates a monthly sales report plot per store and saves it as PNG.
    """
    os.makedirs(output_folder, exist_ok=True)

    # Add time columns
    df['month'] = df['fecha'].dt.month_name()
    df['year'] = df['fecha'].dt.year

    # Aggregate monthly sales
    monthly_sales = df.groupby(['year', 'month', 'store'])['total_venta'].sum().reset_index()

    # Plot
    plt.figure(figsize=(10,6))
    sns.barplot(x='month', y='total_venta', hue='store', data=monthly_sales)
    plt.title('Monthly Sales per Store')
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_path = os.path.join(output_folder, "sales_report.png")
    plt.savefig(output_path)
    plt.close()

    print(f"Sales report saved successfully at: {output_path}")
