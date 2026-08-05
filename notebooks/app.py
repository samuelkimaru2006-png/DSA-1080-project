

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os

@st.cache_data
def load_data():
    base_dir = Path(os.getcwd()).parent
    data_path = base_dir / "C:\\Users\\Lisamarie\\.jupyter\\DSA-1080-project\\data\\processed\\crime_data_cleaned.csv"
    return pd.read_csv(data_path)

df = load_data()

st.set_page_config(
    page_title="West Midlands Crime Dashboard",
    page_icon="🚔",
    layout="wide"
)

st.title("🚔 West Midlands Crime Dashboard")
st.write("Interactive dashboard for exploring crime data.")

st.header("First 5 Rows of the Dataset")
st.dataframe(df.head())

st.header("Dataset Overview")

col1, col2 = st.columns(2)

col1.metric("Total Records", len(df))
col2.metric("Total Columns", len(df.columns))

if "Crime type" in df.columns:

    st.sidebar.header("Filter")

    selected_crime = st.sidebar.selectbox(
        "Select Crime Type",
        ["All"] + sorted(df["Crime type"].dropna().unique())
    )

    if selected_crime != "All":
        df = df[df["Crime type"] == selected_crime]


if "Crime type" in df.columns:

    st.header("Crime Count by Type")

    crime_counts = df["Crime type"].value_counts()

    fig, ax = plt.subplots(figsize=(10,5))
    crime_counts.plot(kind="bar", ax=ax)

    ax.set_xlabel("Crime Type")
    ax.set_ylabel("Number of Crimes")

    st.pyplot(fig)

if "Last outcome category" in df.columns:

    st.header("Crime Outcomes")

    outcome_counts = df["Last outcome category"].value_counts()

    fig, ax = plt.subplots(figsize=(10,5))
    outcome_counts.plot(kind="bar", ax=ax)

    ax.set_xlabel("Outcome")
    ax.set_ylabel("Count")

    st.pyplot(fig)
st.header("Summary Statistics")
st.write(df.describe(include="all"))
st.header("Filtered Dataset")
st.dataframe(df)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_crime_data.csv",
    mime="text/csv"
)