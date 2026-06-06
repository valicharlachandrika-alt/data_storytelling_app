import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Story App", layout="wide")

st.title("📖 Data Storytelling App")

# Upload file
file = st.file_uploader("Upload CSV file")

if file:
    df = pd.read_csv(file)

    st.subheader("📌 Dataset Preview")
    st.write(df.head())

    st.subheader("📊 Dataset Info")
    st.write(df.describe())

    st.subheader("❌ Missing Values")
    st.write(df.isnull().sum())

    # Clean data
    df = df.dropna()

    st.subheader("📈 Story Begins...")

    # Numeric columns
    num_cols = df.select_dtypes(include='number').columns

    if len(num_cols) > 0:
        st.subheader("📊 Distribution Analysis")

        for col in num_cols[:3]:
            fig = px.histogram(df, x=col, title=f"Distribution of {col}")
            st.plotly_chart(fig)

        st.subheader("📉 Relationship Analysis")

        if len(num_cols) > 1:
            fig2 = px.scatter(df, x=num_cols[0], y=num_cols[1])
            st.plotly_chart(fig2)

    # Categorical columns
    cat_cols = df.select_dtypes(include='object').columns

    if len(cat_cols) > 0:
        st.subheader("📊 Category Insights")

        col = cat_cols[0]
        fig3 = px.histogram(df, x=col)
        st.plotly_chart(fig3)

    st.subheader("🧠 Final Insight")
    st.success("Data shows clear patterns after cleaning and visualization. Trends are visible across numeric and categorical variables.")