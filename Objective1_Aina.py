import plotly.express as px
import streamlit as st

# 1. Prepare the data
gender_counts = df['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'count']

# 2. Create the Plotly figure
fig = px.pie(
    gender_counts, 
    values='count', 
    names='gender', 
    title='Distribution of Gender',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    hole=0 # Set to 0.4 for a donut chart!
)

# 3. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
