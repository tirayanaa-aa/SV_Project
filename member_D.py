import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit as st

# --- 1. Scatter Plot with Trendline ---
def create_scatter_plot(df):
    fig = px.scatter(
        df, 
        x='PP_score', 
        y='OIB_score',
        trendline="ols",  # Built-in Ordinary Least Squares regression
        opacity=0.6,
        title='Relationship between Product Presentation and Impulse Buying Behavior on TikTok Shop',
        labels={
            'PP_score': 'Product Presentation Score (Visual Quality & Information)',
            'OIB_score': 'Impulse Buying Score (Spontaneous Purchasing)'
        },
        template='plotly_white'
    )
    fig.update_layout(title_font_size=16)
    return fig

# --- 2. Correlation Heatmap ---
def create_correlation_heatmap(df):
    corr = df[['SL_score','PP_score','OIB_score']].corr()
    
    fig = px.imshow(
        corr,
        text_auto='.2f', # Show values on heatmap
        color_continuous_scale='RdBu_r', # Red-Blue reversed
        range_color=[-1, 1],
        title='Correlation: Shopping Lifestyle, Product Presentation, and Impulse Buying',
        labels={'color': 'Correlation (r)'},
        template='plotly_white'
    )
    fig.update_layout(xaxis_title="Constructs", yaxis_title="Constructs")
    return fig

# --- 3. Stacked Likert Bar Chart ---
def create_likert_stacked_bar(df):
    likert_cols = [
        'image_quality_influence', 'product_description_quality',
        'multi_angle_visuals', 'info_richness_support'
    ]
    
    # Melt the dataframe to make it "long-form" for Plotly
    df_melted = df[likert_cols].melt(var_name='Item', value_name='Response')
    
    # Group and count
    df_counts = df_melted.groupby(['Item', 'Response']).size().reset_index(name='Count')
    
    fig = px.bar(
        df_counts, 
        x='Item', 
        y='Count', 
        color='Response',
        title='Response Distribution for Product Presentation Items',
        labels={'Count': 'Number of Respondents', 'Item': 'Product Presentation Items'},
        barmode='stack',
        template='plotly_white'
    )
    return fig

# --- 4. Grouped Histogram ---
def create_purchase_behavior_hist(df):
    behavior_cols = ['no_purchase_plan', 'no_purchase_intent', 'impulse_purchase']
    df_melted = df[behavior_cols].melt(var_name='Behavior', value_name='Agreement')
    
    fig = px.histogram(
        df_melted, 
        x='Agreement', 
        color='Behavior',
        barmode='group',
        nbins=5,
        title='Distribution of Purchase Behavior on TikTok Shop',
        labels={'Agreement': 'Agreement Level (1=SD, 5=SA)', 'count': 'Number of Respondents'},
        template='plotly_white'
    )
    fig.update_layout(xaxis=dict(tickmode='linear', tick0=1, dtick=1))
    return fig

# --- 5. Box Plot ---
def create_attraction_boxplot(df):
    columns_to_plot = [
        'similar_to_famous_brand_attraction', 'new_product_urgency',
        'brand_trust_influence', 'unique_design_attraction'
    ]
    df_melted = df[columns_to_plot].melt(var_name='Factor', value_name='Score')
    
    fig = px.box(
        df_melted, 
        x='Factor', 
        y='Score', 
        color='Factor',
        title='Distribution of Product Attraction & Trust Factors',
        labels={'Score': 'Score (1=SD, 5=SA)'},
        template='plotly_white'
    )
    fig.update_layout(showlegend=False, xaxis_tickangle=-20)
    return fig

# --- Main App Function ---
def app():
    st.title("TikTok Shop Analysis Dashboard")
    
    # Pastikan data tersedia (Contoh menggunakan session state atau upload)
    if 'df' in st.session_state:
        df = st.session_state.df
        
        st.plotly_chart(create_scatter_plot(df), use_container_width=True)
        st.plotly_chart(create_correlation_heatmap(df), use_container_width=True)
        st.plotly_chart(create_likert_stacked_bar(df), use_container_width=True)
        st.plotly_chart(create_purchase_behavior_hist(df), use_container_width=True)
        st.plotly_chart(create_attraction_boxplot(df), use_container_width=True)
    else:
        st.error("Dataframe tidak ditemukan. Pastikan data sudah dimuat di app.py.")
