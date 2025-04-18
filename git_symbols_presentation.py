import streamlit as st
import pandas as pd
import altair as alt

# Sample mock data — replace with real data
data = {
    "Year": [2021, 2022, 2023, 2024, 2025] * 5,
    "Language": ["Python"]*5 + ["JavaScript"]*5 + ["Java"]*5 + ["C#"]*5 + ["C++"]*5,
    "Popularity (%)": [
        29.9, 31.1, 32.5, 33.2, 34.0,     # Python
        19.8, 20.1, 20.4, 21.0, 21.3,     # JavaScript
        16.5, 16.3, 15.9, 15.5, 15.2,     # Java
        10.2, 10.5, 10.4, 10.6, 10.7,     # C#
        9.8, 9.6, 9.5, 9.3, 9.2           # C++
    ]
}

df = pd.DataFrame(data)

# Title
st.title("Top 5 Programming Languages: Popularity Over the Last 5 Years")

# Sidebar filter
languages = st.multiselect("Select languages to display:", df["Language"].unique(), default=df["Language"].unique())

filtered_df = df[df["Language"].isin(languages)]

# Line chart using Altair
chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x="Year:O",
    y="Popularity (%):Q",
    color="Language:N",
    tooltip=["Year", "Language", "Popularity (%)"]
).properties(
    width=700,
    height=400
)

st.altair_chart(chart, use_container_width=True)

# Data preview
with st.expander("Show raw data"):
    st.dataframe(filtered_df)
