# Crime Data Analysis of the West Midlands Street Crime Dataset (October 2024)

## Project Description

This project analyzes crime data reported by West Midlands Police for October 2024 using Python. The project involves cleaning the dataset, performing exploratory data analysis (EDA), creating visualizations, and developing an interactive Streamlit dashboard to present the findings.



## Problem Statement

Crime datasets contain large amounts of information that can be difficult to interpret without proper analysis. This project aims to analyze reported crimes to identify common crime types, crime hotspots, neighbourhoods with the highest crime rates, and the outcomes of reported crimes. The findings can help provide a better understanding of crime patterns within the West Midlands.



## Dataset

- **Source:** UK Police Data (West Midlands Street Crime Dataset – October 2024)
- **Number of rows:** 28,444
- **Number of columns:** 11

### Key Columns

- Crime ID
- Month
- Reported by
- Falls within
- Longitude
- Latitude
- Location
- LSOA Name
- Crime Type
- Last Outcome Category



## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit
- Git & GitHub


## Data Cleaning

The following cleaning steps were performed:

- Removed duplicate records.
- Checked for missing values.
- Renamed columns to improve readability.
- Verified data types using `df.info()`.
- Identified numerical outliers using the IQR method.
- Created a cleaned dataset for analysis.
- Exported the cleaned dataset to the `data/processed` folder.



## Analysis Questions

The project answered the following questions:

1. What are the most common types of crime?
2. Which locations recorded the highest number of crimes?
3. Which LSOAs (neighbourhoods) experienced the highest crime rates?
4. Which police force recorded the highest number of reported crimes?
5. How are crime locations distributed geographically?
6. What percentage of crimes fall into each crime category?
7. What are the most common crime outcomes?
8. Is there a relationship between crime type and crime outcome?
9. Which crime types are most common in the top 10 high-crime neighbourhoods?
10. What percentage of crimes resulted in each outcome category?



## Visualizations

The project includes the following visualizations:

- Bar chart showing the number of crimes by crime type.
- Horizontal bar chart of the top 10 crime outcomes.
- Pie chart showing the percentage distribution of crime types.
- Scatter plot showing the geographical distribution of crime locations.
- Heatmap illustrating the relationship between crime types and crime outcomes.
- Stacked bar chart showing crime types across the top 10 high-crime LSOAs.
- Box plot used to identify longitude outliers during data cleaning.

All visualizations are stored in the **visuals/** folder.



## Key Insights

1. Violence and sexual offences were the most frequently reported crimes.
2. Crime was concentrated in a relatively small number of neighbourhoods (LSOAs).
3. The majority of reported crimes came from the West Midlands Police area.
4. Different crime types showed different outcome patterns, as observed in the heatmap.
5. Crime locations formed geographical clusters rather than being evenly distributed.



## Recommendations

Based on the analysis, the following recommendations are suggested:

- Allocate additional police resources to high-crime neighbourhoods.
- Increase crime prevention initiatives targeting violence and sexual offences.
- Monitor crime hotspots regularly using geographical analysis.
- Investigate crime categories with low resolution rates to improve policing strategies.
- Continue collecting and analysing crime data to monitor trends over time.



## How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/samuelkimaru2006-png/DSA-1080-project.git
```

2. Navigate to the project folder

```bash
cd DSA-1080-project
```

3. Install the required libraries

```bash
pip install -r requirements.txt
```

4. Open the Jupyter Notebook

```bash
jupyter notebook
```

5. Open `analysis.ipynb` and run all cells.

6. To launch the interactive dashboard, run:

```bash
python -m streamlit run app.py
```


## Authors

**Samuel Kimaru**  
**Registration Number:** *[202601196]*

**LisaMarie Wanderwa**  
**Registration Number:** *[676685]*
