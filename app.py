import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure the page
st.set_page_config(
    page_title="West Midlands Crime Dashboard",
    page_icon="🚔",
    layout="wide"
)

# Dashboard title
st.title("🚔 West Midlands Crime Dashboard")

# Short description
st.write(
    "This dashboard presents an analysis of the West Midlands Police crime dataset."
)
import streamlit as st
import pandas as pd

# Configure the page
st.set_page_config(
    page_title="West Midlands Crime Dashboard",
    page_icon="🚔",
    layout="wide"
)

# Load the cleaned dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/crime_data_cleaned.csv")

df = load_data()

# Dashboard title
st.title("🚔 West Midlands Crime Dashboard")

st.write("This dashboard presents an analysis of the West Midlands Police crime dataset.")

# Show first few rows
st.subheader("Dataset Preview")
st.dataframe(df.head())
# Sidebar Filters
st.sidebar.header("Filters")

# Crime Type filter
crime_types = ["All"] + sorted(df["Crime_Type"].unique().tolist())

selected_crime = st.sidebar.selectbox(
    "Select Crime Type",
    crime_types
)

# Crime Outcome filter
outcomes = ["All"] + sorted(df["Last_Outcome_Category"].unique().tolist())

selected_outcome = st.sidebar.selectbox(
    "Select Crime Outcome",
    outcomes
)

# LSOA filter
lsoas = ["All"] + sorted(df["LSOA_Name"].unique().tolist())

selected_lsoa = st.sidebar.selectbox(
    "Select LSOA",
    lsoas
)

# Apply Filters

filtered_df = df.copy()

if selected_crime != "All":
    filtered_df = filtered_df[
        filtered_df["Crime_Type"] == selected_crime
    ]

if selected_outcome != "All":
    filtered_df = filtered_df[
        filtered_df["Last_Outcome_Category"] == selected_outcome
    ]

if selected_lsoa != "All":
    filtered_df = filtered_df[
        filtered_df["LSOA_Name"] == selected_lsoa
    ]
st.dataframe(df.head())
st.subheader("Filtered Dataset")

st.write(f"Number of records: {len(filtered_df)}")

st.dataframe(filtered_df)
# Dashboard Summary
st.subheader("Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Crimes",
    len(filtered_df)
)

col2.metric(
    "Crime Types",
    filtered_df["Crime_Type"].nunique()
)

col3.metric(
    "Neighbourhoods",
    filtered_df["LSOA_Name"].nunique()
)

col4.metric(
    "Police Outcomes",
    filtered_df["Last_Outcome_Category"].nunique()
)

# Crime Types


st.subheader("Most Common Crime Types")

fig, ax = plt.subplots(figsize=(10, 6))

filtered_df["Crime_Type"].value_counts().plot(
    kind="bar",
    ax=ax,
    color="steelblue"
)

ax.set_title("Number of Crimes by Crime Type")
ax.set_xlabel("Crime Type")
ax.set_ylabel("Number of Crimes")

plt.xticks(rotation=45, ha="right")

st.pyplot(fig)
st.subheader("Crime Type Distribution")

crime_percent = (
    filtered_df["Crime_Type"]
    .value_counts(normalize=True) * 100
)

fig, ax = plt.subplots(figsize=(9, 8))

# Draw the pie chart WITHOUT percentages
wedges, _ = ax.pie(
    crime_percent,
    startangle=90
)

# Create legend labels with percentages
legend_labels = [
    f"{crime}: {percent:.1f}%"
    for crime, percent in zip(crime_percent.index, crime_percent.values)
]

ax.legend(
    wedges,
    legend_labels,
    title="Crime Type",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

ax.set_title("Percentage Distribution of Crime Types")

st.pyplot(fig)
legend_labels = [
    f"{crime}: {percent:.1f}%"
    for crime, percent in zip(crime_percent.index, crime_percent.values)
]
st.subheader("Crime Type vs Crime Outcome")

crime_outcome = pd.crosstab(
    filtered_df["Crime_Type"],
    filtered_df["Last_Outcome_Category"]
)

fig, ax = plt.subplots(figsize=(14, 7))

sns.heatmap(
    crime_outcome,
    cmap="Blues",
    annot=False,
    linewidths=0.5,
    ax=ax
)

ax.set_xlabel("Crime Outcome")
ax.set_ylabel("Crime Type")

st.pyplot(fig)
st.subheader("Top 10 High-Crime Neighbourhoods")

top_lsoa = (
    filtered_df["LSOA_Name"]
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,6))

top_lsoa.plot(
    kind="bar",
    color="teal",
    ax=ax
)

ax.set_title("Top 10 High-Crime LSOAs")
ax.set_xlabel("LSOA")
ax.set_ylabel("Number of Crimes")

plt.xticks(rotation=45, ha="right")

st.pyplot(fig)
st.subheader("Crime Outcomes")

outcomes = (
    filtered_df["Last_Outcome_Category"]
    .value_counts(normalize=True) * 100
)

fig, ax = plt.subplots(figsize=(10,6))

outcomes.plot(
    kind="barh",
    color="orange",
    ax=ax
)

ax.set_xlabel("Percentage of Crimes")
ax.set_ylabel("Outcome")

st.pyplot(fig)
st.subheader("Crime Locations")

fig, ax = plt.subplots(figsize=(10,6))

ax.scatter(
    filtered_df["Longitude"],
    filtered_df["Latitude"],
    alpha=0.4,
    s=10
)

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("Crime Locations")

st.pyplot(fig)
st.subheader("Filtered Dataset")

st.write(f"Records shown: {len(filtered_df)}")

st.dataframe(filtered_df)
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="filtered_crime_data.csv",
    mime="text/csv"
)
st.subheader("Key Insights")

st.markdown("""
- Violence and sexual offences account for the largest proportion of recorded crimes.
- Crime is concentrated in a relatively small number of neighbourhoods.
- Some police outcomes occur much more frequently than others.
- Different crime types are associated with different recorded outcomes.
- Geographic coordinates show clusters of reported crime locations.
""")