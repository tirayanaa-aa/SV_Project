import streamlit as st

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Visualization",
    layout="wide"
)

# ------------------------------------------------------------
# Title
# ------------------------------------------------------------
st.title("📊 Determinants of Students’ Impulse Buying Behavior on TikTok Shop")

st.markdown("---")

# ------------------------------------------------------------
# Project Overview
# ------------------------------------------------------------
st.header("📌 Project Overview")
st.write("""
This project investigates **students’ impulse buying behavior on TikTok Shop** using 
survey data and **scientific visualization techniques**.  

Impulse buying has become increasingly common on social commerce platforms like TikTok Shop, 
where entertainment, promotions, and instant purchasing are combined in a single environment.
Through interactive visualizations, this project aims to uncover patterns, relationships, 
and insights behind students’ purchasing behavior.
""")

# ------------------------------------------------------------
# Problem Statement
# ------------------------------------------------------------
st.header("❗ Problem Statement")
st.write("""
TikTok Shop has gained rapid popularity among students due to its engaging content, 
time-limited promotions, and visually appealing product presentations. As a result, 
many students make **unplanned and impulsive purchases** without careful evaluation.

However, students are often unaware of the psychological and platform-related factors 
that influence their impulse buying behavior. At the same time, sellers and marketers 
lack clear visual insights into these behaviors. Without proper data visualization, 
important patterns and relationships within impulse buying behavior remain hidden.
""")

# ------------------------------------------------------------
# Project Objectives
# ------------------------------------------------------------
st.header("🎯 Project Objectives")
st.write("""
**Main Objective:**  
To analyze and visualize the factors influencing online impulse buying behavior on TikTok Shop 
using scientific data visualization techniques.

**Sub-Objectives:**  
1. Analyze the demographic profile and TikTok Shop usage among students.  
2. Evaluate the influence of scarcity and unexpected product discovery on shopping behavior.  
3. Examine the role of **trust, enjoyment, and shopping motivation** on TikTok Shop.  
4. Analyze product presentation, lifestyle factors, and impulse buying behavior.
""")

# --------------------------------------------------
# Dataset Description
# --------------------------------------------------
st.subheader("📂 Dataset Description")
st.write("""
The dataset consists of survey responses collected from university students
using Google Forms.

- Data type: Likert-scale questionnaire  
- Respondents: University students  
- Focus: TikTok Shop shopping experience and behavior  
- Data preprocessing: Cleaning, renaming, and composite score calculation
""")

st.markdown("---")

# --------------------------------------------------
# Tools & Techniques
# --------------------------------------------------
st.subheader("🛠 Tools & Techniques")
st.markdown("""
- **Python** – Data processing and analysis  
- **Streamlit** – Interactive dashboard development  
- **Pandas** – Data manipulation  
- **Plotly / Matplotlib / Seaborn** – Scientific visualizations  
""")

st.markdown("---")

# --------------------------------------------------
# Navigation Guide
# --------------------------------------------------
st.subheader("🧭 Navigation Guide")
st.write("""
Use the **sidebar** to navigate through different sections of the dashboard:

- **Main Page** – Project overview and objectives  
- **Member Pages** – Each member focuses on a specific sub-objective  
  - Member A: Demographic profile & usage  
  - Member B: Scarcity & product discovery  
  - Member C: Trust & shopping motivation  
  - Member D: Product presentation & impulse buying
""")

st.info("📌 Please use the sidebar on the left to explore the analysis pages.")

# ------------------------------------------------------------
# Academic Note
# ------------------------------------------------------------
st.markdown("---")
st.info("""
📘 **Academic Note:**  
This project is conducted for educational purposes only.  
All data is anonymized and analyzed ethically to support learning in data visualization.
""")

