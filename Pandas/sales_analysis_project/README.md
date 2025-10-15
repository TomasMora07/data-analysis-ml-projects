Sales Data Analysis Project
End-to-End Data Analysis and ETL Pipeline (Python + Pandas)

This project demonstrates a complete data workflow — from raw CSV files to clean, validated, and visualized insights.
It simulates a real-world ETL (Extract, Transform, Load) process for sales data from two different stores.

The goal is to ensure data quality, consistency, and automation, using tools and practices aligned with professional data operations.

Project Overview

The analysis covers two sales datasets containing daily transactions for two stores.
The process consolidates, cleans, and analyzes the data to generate key metrics and visual reports.

ETL Pipeline Steps
Step	         Description
1. Extract	     Load raw CSV files (Store_Sales_Data.csv and Store_Sales_Data2.csv) from the /data/raw/ folder.
2. Transform	 Standardize column names, clean null and invalid values, fix data types, and calculate total sales.
3. Validate	     Check for missing, duplicate, or negative values to ensure data integrity.
4. Load	         Save the cleaned and merged dataset to /data/processed/merged_sales.csv.
5. Visualize	 Generate a bar chart comparing monthly sales by store, saved as /outputs/sales_report.png.

Technologies Used

-Python 3.12
-Pandas → data manipulation and cleaning
-NumPy → numeric processing
-Matplotlib / Seaborn → data visualization
-Jupyter Notebook → analysis and documentation
-Modular ETL scripts → (src/etl_pipeline.py and src/utils.py)

Key Features

-Combine multiple data sources
-Perform data validation and type conversion
-Recalculate metrics to ensure consistency
-Automate ETL steps through modular scripts
-Create professional visualizations and reports

Example Output:
Monthly Sales per Store (2024)


Results Summary

-Cleaned and consolidated over 3,000 sales records from two stores.
-Identified top-performing months and products.
-Automated ETL pipeline ready for scaling or deployment.

Learning Outcomes

This project demonstrates:
-How to build a scalable and maintainable data workflow.
-How to ensure data integrity before analysis.
-How to apply Python data tools in a real business context.

“I designed this project to simulate professional data operations — combining raw data extraction, cleaning, transformation, validation, and visualization into one reproducible workflow.”

Author: Tomás Mora
Software Engineering & Data Analysis Student
Costa Rica