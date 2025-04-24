import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("Iris Data Analysis")

# Load the dataset
df = pd.read_csv("data/Iris.csv")

# Check if data is loaded
if df.empty:
    st.warning("Failed to load data.")
    st.stop()

# Display first rows of the dataset
st.subheader("First rows of the dataset")
st.dataframe(df.head())

# Slider for filtering by sepal length
threshold = st.slider("Minimum Sepal Length (cm)", 4.0, 8.0, 5.0)

# Filter data based on slider value
filtered_df = df[df["SepalLengthCm"] >= threshold]

# Scatter plot of filtered data
st.subheader("Filtered Data Visualization")
fig = px.scatter(
    filtered_df,
    x="SepalLengthCm",
    y="SepalWidthCm",
    color="Species",
    title="Sepal Length vs Sepal Width",
    labels={"SepalLengthCm": "Sepal Length (cm)", "SepalWidthCm": "Sepal Width (cm)"},
)
st.plotly_chart(fig)
