import pandas as pd
import plotly.express as px

# =========================
# 1. SCATTER PLOT + TREND LINE
# =========================
fig1 = px.scatter(
    df,
    x='PP_score',
    y='OIB_score',
    trendline='ols',
    title='Relationship between Product Presentation<br>and Impulse Buying Behavior on TikTok Shop',
    labels={
        'PP_score': 'Product Presentation Score (Visual Quality & Information)',
        'OIB_score': 'Impulse Buying Score (Spontaneous Purchasing)'
    }
)
fig1.show()


# =========================
# 2. CORRELATION HEATMAP
# =========================
corr = df[['SL_score', 'PP_score', 'OIB_score']].corr()

fig2 = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale='RdBu',
    zmin=-1,
    zmax=1,
    title='Correlation between Shopping Lifestyle, Product Presentation,<br>and Impulse Buying Behavior on TikTok Shop'
)
fig2.show()


# =========================
# 3. LIKERT STACKED BAR CHART
# =========================
likert_data = df[
    ['image_quality_influence',
     'product_description_quality',
     'multi_angle_visuals',
     'info_richness_support']
]

likert_long = likert_data.melt(
    var_name='Product Presentation Item',
    value_name='Agreement Level'
)

fig3 = px.histogram(
    likert_long,
    x='Product Presentation Item',
    color='Agreement Level',
    barmode='stack',
    title='Response Distribution for Product Presentation Items'
)

fig3.update_layout(
    yaxis_title='Number of Respondents',
    xaxis_title='Product Presentation Items'
)

fig3.show()


# =========================
# 4. MULTI HISTOGRAM – PURCHASE BEHAVIOR
# =========================
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
    title='Distribution of Purchase Behavior on TikTok Shop'
)

fig4.update_layout(
    xaxis=dict(tickmode='linear', tick0=1, dtick=1),
    yaxis_title='Number of Respondents'
)

fig4.show()


# =========================
# 5. BOX PLOT – PRODUCT & BRAND FACTORS
# =========================
box_long = df.melt(
    value_vars=[
        'similar_to_famous_brand_attraction',
        'new_product_urgency',
        'brand_trust_influence',
        'unique_design_attraction'
    ],
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

fig5.show()
