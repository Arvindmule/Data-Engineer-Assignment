
This project utilizes PostgreSQL and Python to analyze movie datasets sourced from CSV files. The goal is to uncover insightful trends and statistics within the movie industry by conducting various analyses on movie and rating data.

## Overview

- **Database Setup:** Establishes a PostgreSQL database to store movie and rating information.
- **Data Import:** Imports CSV files into the PostgreSQL database for analysis.
- **Insights & Analysis:** Utilizes Python scripting and SQL queries to perform detailed analyses, including identifying top movies by different criteria, rater insights, trend spotting, and individual preferences.
- **Efficient Execution:** A well-commented Python script drives efficient execution, ensuring clarity in code logic and assumptions.

## Key Tasks

1. **Setup:**
   - Establish PostgreSQL database.
   - Create tables for movie and rating data.

2. **Data Import:**
   - Import movie and rating data from CSV files.

3. **Analysis Highlights:**
   - Top movies based on duration, year, and average rating.
   - Unique rater counts and top raters.
   - Top-rated movies under specific conditions (e.g., director, genre, year, country).
   - Individual preferences and rater-specific analyses.
   - Trends like specific year insights and genre preferences.
   - Identification of high-rated movies meeting certain criteria.

## How to Use

1. **Setup:**
   - Ensure PostgreSQL is installed.
   - Create a database and tables using the provided SQL schema.

2. **Execution:**
   - Execute the Python script `data_analysis.py`.
   - Update database credentials in the script if needed.
   - Run the script to perform the analyses.

3. **Results:**
   - Results and insights will be displayed in the console or specified output.

## Assumptions

- CSV files contain properly formatted data.
- The PostgreSQL database is set up and accessible.
- Python and necessary libraries (e.g., `psycopg2`) are installed.

## Contribution

Contributions and improvements are welcome! Feel free to fork this repository, make changes, and submit a pull request.
