
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Food Macro Comparison",
    page_icon="🍗",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("foods.csv")

df = load_data()

st.title("🍎 Food Macro Comparison App")
st.write("Compare calories and macros of 100+ foods.")

st.sidebar.header("Filters")

metric = st.sidebar.selectbox(
    "Sort By",
    ["Calories", "Protein", "Carbs", "Fat", "Fiber"]
)

min_protein = st.sidebar.slider(
    "Minimum Protein (g)",
    0,
    50,
    0
)

filtered_df = df[df["Protein"] >= min_protein]

st.subheader("Food Database")

st.dataframe(
    filtered_df.sort_values(metric, ascending=False),
    use_container_width=True
)

st.subheader("Compare Foods")

selected_foods = st.multiselect(
    "Select up to 5 foods",
    df["Food"].tolist(),
    max_selections=5
)

if selected_foods:
    compare_df = df[df["Food"].isin(selected_foods)]

    st.dataframe(compare_df, use_container_width=True)

    fig = px.bar(
        compare_df,
        x="Food",
        y=["Calories", "Protein", "Carbs", "Fat"],
        barmode="group",
        title="Macro Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Top High Protein Foods")

top_protein = df.sort_values(
    "Protein",
    ascending=False
).head(10)

fig2 = px.bar(
    top_protein,
    x="Food",
    y="Protein",
    title="Top 10 Protein Rich Foods"
)

st.plotly_chart(fig2, use_container_width=True)
