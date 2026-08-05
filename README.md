# Crime Data Analysis

## Group Members

- Samuel Mwangi
- LisaMarie Wanderwa


# Project Description

This project analyzes street crime data reported by West Midlands Police for October 2024. The objective is to clean the dataset, explore crime patterns, create visualizations, and build an interactive dashboard using Streamlit.

The project was completed as part of the DSA 1080 Programming for Data Science course.


# Dataset

**Dataset:** West Midlands Street Crime Dataset (October 2024)

The dataset contains information such as:

- Crime ID
- Month
- Police Force
- Location
- LSOA (Neighbourhood)
- Crime Type
- Longitude
- Latitude
- Last Outcome Category


# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook
- Git & GitHub

# Project Structure

DSA-1080-project/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── analysis.ipynb
│
└── visuals/

# Data Cleaning

The dataset was prepared by:

- Removing duplicate records
- Checking for missing values
- Renaming columns
- Formatting the Month column
- Creating a cleaned dataset for analysis


# Analysis Questions

The project answers questions such as:

1. What are the most common crime types?
2. Which locations have the highest number of crimes?
3. Which neighbourhoods (LSOAs) experience the highest crime levels?
4. What percentage of crimes fall into each category?
5. What are the most common crime outcomes?
6. Is there a relationship between crime type and crime outcome?
7. Which crime types are most common in the top 10 high-crime LSOAs?
8. What percentage of crimes resulted in each outcome category?
9. Which crime outcome occurs most frequently?



# Visualizations

The project includes:

- Bar Chart
- Pie Chart
- Heatmap
- Horizontal Bar Chart
- Scatter Plot
- Box Plot

All charts are saved in the **visuals/** folder.



# Key Insights

- Violence and sexual offences were the most frequently reported crimes.
- Shoplifting and vehicle crime were among the next most common crime categories.
- Crime was concentrated in a small number of neighbourhoods.
- Different crime types showed different outcome patterns.
- Geographic data showed clusters of crime locations.



# Interactive Dashboard

A Streamlit dashboard was developed to allow users to:

- Filter crime data
- View summary statistics
- Explore interactive visualizations
- Browse the cleaned dataset
- Download filtered data



# Running the Project

Clone the repository:

bash
git clone https://github.com/samuelkimaru2006-png/DSA-1080-project.git


Install the required packages:

bash
pip install -r requirements.txt


Run the dashboard:
bash
python -m streamlit run app.py


# Repository

https://github.com/samuelkimaru2006-png/DSA-1080-project
