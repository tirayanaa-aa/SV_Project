import streamlit as st
import pandas as pd
import plotly.express as px

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Study",
    layout="wide"
)

st.title("📊 Determinants of Students' Impulse Buying Behavior on TikTok Shop")
st.write("This dashboard presents interactive visualizations analysing factors that influence students' impulse buying behaviour on TikTok Shop.")

# =============================
# LOAD DATA
# =============================
@st.cache_data
def load_data():
    return pd.read_excel("clean_impulse_buying_data.xlsx")

df = load_data()

st.markdown("---")

# =============================
# 1. SCATTER PLOT + TREND LINE
# =============================
st.subheader("1️⃣ Relationship Between Product Presentation and Impulse Buying")

fig1 = px.scatter(
    df,
    x='PP_score',
    y='OIB_score',
    trendline='ols',
    labels={
        'PP_score': 'Product Presentation Score',
        'OIB_score': 'Impulse Buying Score'
    },
    title='Product Presentation vs Impulse Buying'
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# =============================
# 2. CORRELATION HEATMAP
# =============================
st.subheader("2️⃣ Correlation Between Key Constructs")

corr = df[['SL_score', 'PP_score', 'OIB_score']].corr()

fig2 = px.imshow(
    corr,
    text_auto='.2f',
    zmin=-1,
    zmax=1,
    color_continuous_scale='RdBu',
    title='Correlation Matrix'
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# =============================
# 3. LIKERT STACKED BAR CHART
# =============================
st.subheader("3️⃣ Product Presentation Item Responses")

likert_cols = [
    'image_quality_influence',
    'product_description_quality',
    'multi_angle_visuals',
    'info_richness_support'
]

likert_long = df[likert_cols].melt(
    var_name='Item',
    value_name='Agreement Level'
)

fig3 = px.histogram(
    likert_long,
    x='Item',
    color='Agreement Level',
    barmode='stack',
    title='Likert Scale Response Distribution'
)

fig3.update_layout(
    xaxis_title='Product Presentation Items',
    yaxis_title='Number of Respondents'
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# =============================
# 4. PURCHASE BEHAVIOUR HISTOGRAM
# =============================
st.subheader("4️⃣ Purchase Behaviour Distribution")

purchase_long = df.melt(
    value_vars=['no_purchase_plan', 'no_purchase_intent', 'impulse_purchase'],
    var_name='Purchase Type',
    value_name='Score'
)

fig4 = px.histogram(
    purchase_long,
    x='Score',
    color='Purchase Type',
    barmode='overlay',
    nbins=5,
    title='Distribution of Purchase Behaviour'
)

fig4.update_layout(
    xaxis=dict(tickmode='linear', tick0=1, dtick=1),
    yaxis_title='Number of Respondents'
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# =============================
# 5. BOX PLOT – PRODUCT & BRAND FACTORS
# =============================
st.subheader("5️⃣ Product & Brand Attraction Factors")

box_cols = [
    'similar_to_famous_brand_attraction',
    'new_product_urgency',
    'brand_trust_influence',
    'unique_design_attraction'
]

box_long = df[box_cols].melt(
    var_name='Factor',
    value_name='Score'
)

fig5 = px.box(
    box_long,
    x='Factor',
    y='Score',
    points='outliers',
    title='Distribution of Product Attraction & Trust Factors'
)

fig5.update_layout(
    yaxis_title='Score (1 = Strongly Disagree, 5 = Strongly Agree)'
)

st.plotly_chart(fig5, use_container_width=True)
