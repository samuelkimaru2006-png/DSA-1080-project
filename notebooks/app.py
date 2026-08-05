


import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path



st.set_page_config(
    page_title="West Midlands Crime Dashboard",
    page_icon="🚔",
    layout="wide"
)



@st.cache_data
def load_data():

    data_path = Path(
        r"C:\Users\Lisamarie\.jupyter\DSA-1080-project\data\processed\crime_data_cleaned.csv"
    )

    return pd.read_csv(data_path)


df = load_data()



st.title("🚔 West Midlands Crime Dashboard")

st.markdown("""
### About this dashboard

This interactive dashboard explores West Midlands crime data.
It provides insights into:

- Crime patterns
- Most common crime categories
- Crime outcomes
- Trends over time
""")

st.divider()



st.sidebar.header("🔎 Filters")


filtered_df = df.copy()


# Crime filter
if "Crime type" in df.columns:

    crime_options = sorted(
        df["Crime type"]
        .dropna()
        .unique()
    )

    selected_crime = st.sidebar.multiselect(
        "Select Crime Type",
        crime_options
    )

    if selected_crime:
        filtered_df = filtered_df[
            filtered_df["Crime type"]
            .isin(selected_crime)
        ]


# Outcome filter
if "Last outcome category" in df.columns:

    outcome_options = sorted(
        df["Last outcome category"]
        .dropna()
        .unique()
    )

    selected_outcome = st.sidebar.multiselect(
        "Select Outcome",
        outcome_options
    )

    if selected_outcome:
        filtered_df = filtered_df[
            filtered_df["Last outcome category"]
            .isin(selected_outcome)
        ]




st.header("📊 Key Statistics")


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Crimes",
    f"{len(filtered_df):,}"
)


if "Crime type" in filtered_df.columns:

    col2.metric(
        "Crime Categories",
        filtered_df["Crime type"].nunique()
    )


    col3.metric(
        "Most Common Crime",
        filtered_df["Crime type"].mode()[0]
    )


if "Last outcome category" in filtered_df.columns:

    col4.metric(
        "Outcomes",
        filtered_df["Last outcome category"].nunique()
    )


st.divider()




if "Crime type" in filtered_df.columns:

    st.header("📌 Top Crime Types")


    crime_counts = (
        filtered_df["Crime type"]
        .value_counts()
        .head(10)
    )


    fig, ax = plt.subplots(figsize=(10,5))


    crime_counts.sort_values().plot(
        kind="barh",
        ax=ax
    )


    ax.set_xlabel(
        "Number of Crimes"
    )

    ax.set_ylabel(
        "Crime Type"
    )


    st.pyplot(fig)




if "Last outcome category" in filtered_df.columns:


    st.header("⚖️ Crime Outcomes")


    outcome_counts = (
        filtered_df["Last outcome category"]
        .value_counts()
        .head(10)
    )


    fig, ax = plt.subplots(figsize=(10,5))


    outcome_counts.plot(
        kind="bar",
        ax=ax
    )


    ax.set_xlabel(
        "Outcome"
    )

    ax.set_ylabel(
        "Count"
    )


    plt.xticks(
        rotation=45,
        ha="right"
    )


    st.pyplot(fig)




possible_dates = [
    "Month",
    "month",
    "Date",
    "date"
]


date_column = None


for col in possible_dates:

    if col in filtered_df.columns:
        date_column = col



if date_column:


    st.header("📈 Crime Trend Over Time")


    filtered_df[date_column] = pd.to_datetime(
        filtered_df[date_column]
    )


    trend = (
        filtered_df
        .groupby(date_column)
        .size()
    )


    fig, ax = plt.subplots(figsize=(12,5))


    trend.plot(
        kind="line",
        marker="o",
        ax=ax
    )


    ax.set_xlabel(
        "Date"
    )

    ax.set_ylabel(
        "Number of Crimes"
    )


    st.pyplot(fig)




st.divider()


st.header("📋 Dataset Preview")


st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)




st.header("📑 Summary Statistics")


st.dataframe(
    filtered_df.describe(include="all"),
    use_container_width=True
)
csv = filtered_df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="west_midlands_filtered_crime.csv",
    mime="text/csv"
)