import streamlit as st

# --------------------------------------------------
# Page Configuration (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Visualization",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("📊 Determinants of Students’ Impulse Buying Behavior on TikTok Shop")

# --------------------------------------------------
# Project Snapshot
# --------------------------------------------------
st.markdown("""
### 🧾 Project Snapshot
- **Domain:** Social Commerce & Consumer Behavior  
- **Target Group:** University Students  
- **Platform:** TikTok Shop  
- **Data Type:** Survey (Likert-scale)  
- **Analysis Type:** Descriptive & Exploratory Visualization  
- **Total Sub-Objectives:** 4  
""")

st.markdown("---")

# --------------------------------------------------
# Project Overview
# --------------------------------------------------
st.subheader("🎯 Project Overview")
st.write("""
This project investigates **students’ impulse buying behavior on TikTok Shop** using 
survey data and **scientific visualization techniques**.

Impulse buying has become increasingly common on social commerce platforms like TikTok Shop, 
where entertainment, promotions, and instant purchasing are combined in a single environment.
Through interactive visualizations, this project aims to uncover patterns, relationships, 
and insights behind students’ purchasing behavior.
""")

st.markdown("---")

# --------------------------------------------------
# Problem Statement
# --------------------------------------------------
st.subheader("📌 Problem Statement")
st.write("""
TikTok Shop has rapidly gained popularity among students by integrating entertainment,
product discovery, and instant purchasing within a single platform.
As a result, many students engage in impulse buying without prior planning.

However, the factors driving this behavior—such as promotions, trust, enjoyment,
product presentation, and personal shopping lifestyle—are not always clearly understood.
Without proper visualization and analysis, it is difficult to identify patterns,
relationships, and trends within impulse buying behavior.
""")

st.markdown("---")

# --------------------------------------------------
# Project Objectives
# --------------------------------------------------
st.subheader("🎯 Project Objectives")
st.markdown("""
**Main Objective:**  
To analyze and visualize the factors influencing students’ impulse buying behavior
on TikTok Shop using scientific data visualization techniques.

**Sub-Objectives:**
1. Analyze the demographic profile and TikTok Shop usage among students  
2. Evaluate the influence of scarcity and unexpected product discovery  
3. Examine the role of trust, enjoyment, and shopping motivation  
4. Analyze the impact of product presentation and shopping lifestyle on impulse buying behavior
""")

st.markdown("---")

# --------------------------------------------------
# Visualization Strategy
# --------------------------------------------------
st.subheader("📈 Visualization Strategy")
st.write("""
This project applies **scientific visualization principles** to transform raw survey data
into meaningful visual insights. Each visualization is selected based on the
data type and analytical objective.
""")

st.markdown("""
**Visualization Techniques Used:**
- **Bar Charts** – Compare demographic groups and factor importance  
- **Stacked / Grouped Bar Charts** – Compare TikTok Shop usage across demographics  
- **Heatmaps** – Identify correlations between psychological factors  
- **Box Plots** – Analyze response variability and distribution  
- **Scatter Plots** – Examine relationships between trust, motivation, and impulse buying  
- **Radar Charts** – Visualize multi-dimensional trust and motivation constructs
""")

st.markdown("---")

# --------------------------------------------------
# Dashboard Design Rationale
# --------------------------------------------------
st.subheader("🎨 Dashboard Design Rationale")
st.markdown("""
An **interactive dashboard** is chosen instead of static charts to enable
active exploration of patterns and relationships.

**Design Considerations:**
- Interactivity for demographic filtering  
- Multiple coordinated views for comparison  
- Clean layout to reduce cognitive overload  
- Consistent color usage for readability  

**Why Streamlit?**
- Lightweight and reproducible  
- Suitable for academic visualization projects  
- Supports rapid development of interactive dashboards
""")

st.markdown("---")

# --------------------------------------------------
# Methodology Overview
# --------------------------------------------------
st.subheader("🔬 Methodology Overview")
st.markdown("""
1. **Data Collection** – Online questionnaire using Likert-scale items  
2. **Data Cleaning** – Handling missing values and validation  
3. **Feature Construction** – Composite scores for trust, motivation, and impulse buying  
4. **Visualization Design** – Chart selection based on analytical goals  
5. **Interactive Analysis** – Dynamic filtering and exploration  

This workflow ensures insights are **systematic, reproducible, and scientifically grounded**.
""")

st.markdown("---")

# --------------------------------------------------
# Dataset Description
# --------------------------------------------------
st.subheader("📂 Dataset Description")
st.markdown("""
**Dataset Characteristics:**
- Respondents: University students  
- Scale: 5-point Likert scale  
- Variables:
  - Demographics  
  - TikTok Shop usage behavior  
  - Psychological factors  
  - Product presentation & impulse buying indicators
""")

st.markdown("""
**Dataset Summary:**
- Total Respondents: **113 students**  
- Total Variables: **43 variables**  
- Likert Scale: **1 (Strongly Disagree) – 5 (Strongly Agree)**  
- Missing Values: **Removed during cleaning**
""")

st.markdown("---")

# --------------------------------------------------
# Expected Insights
# --------------------------------------------------
st.subheader("🔍 Expected Insights & Outcomes")
st.write("""
This dashboard aims to:
- Identify active TikTok Shop user groups  
- Understand how scarcity and discovery trigger impulse buying  
- Examine trust and enjoyment as purchase motivators  
- Analyze the impact of product presentation on unplanned purchases
""")

st.markdown("---")

# --------------------------------------------------
# Limitations
# --------------------------------------------------
st.subheader("⚠️ Limitations & Assumptions")
st.markdown("""
- Self-reported survey data  
- Student-only sample  
- Cross-sectional design  
- Behavioral intent rather than actual purchase data
""")

st.markdown("---")

# --------------------------------------------------
# Tools
# --------------------------------------------------
st.subheader("🛠 Tools & Techniques")
st.markdown("""
- **Python**  
- **Streamlit**  
- **Pandas**  
- **Plotly / Matplotlib / Seaborn**
""")

st.markdown("---")

# --------------------------------------------------
# Team
# --------------------------------------------------
st.subheader("👥 Project Team & Responsibilities")
st.markdown("""
- **Aina** – Demographics & Usage  
- **Nurin** – Scarcity & Discovery  
- **Nadia** – Trust & Motivation  
- **Athirah** – Presentation & Lifestyle
""")

st.markdown("---")

# --------------------------------------------------
# How to Use
# --------------------------------------------------
st.subheader("🧑‍💻 How to Use This Dashboard")
st.markdown("""
- Use the **sidebar** to navigate between sections  
- Apply filters where available  
- Hover over charts for detailed values  
- Read interpretations below each visualization
""")

st.markdown("---")

# --------------------------------------------------
# Academic Note
# --------------------------------------------------
st.info("""
📘 **Academic Note:**  
This project is conducted for educational purposes only.  
All data is anonymized and analyzed ethically.
""")
