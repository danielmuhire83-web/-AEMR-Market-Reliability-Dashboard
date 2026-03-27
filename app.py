import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Setup
st.set_page_config(page_title="AEMR Dashboard", layout="wide")

# 2. Cached Data Loading
@st.cache_data
def get_data():
    df = pd.read_csv("aemr.csv").drop(columns=['Unnamed: 0'], errors='ignore')
    
    # Clean Dates
    df[["Start_Time", "End_Time"]] = df[["Start_Time", "End_Time"]].apply(pd.to_datetime, errors='coerce')
    df = df.dropna(subset=["Start_Time", "End_Time"])
    
    # --- ADD THESE LINES TO FIX THE ERROR ---
    df['Year'] = df['Start_Time'].dt.year
    df['Month'] = df['Start_Time'].dt.month
    # ----------------------------------------
    
    # Calculate Outage Hours
    df['Outage_Time_Hours'] = (df['End_Time'] - df['Start_Time']).dt.total_seconds() / 3600
    
    # Fill Missing Risk
    df["Risk_Classification"] = df["Risk_Classification"].fillna("Not classified")
    
    return df

df = get_data()

# 3. Sidebar Interactivity
st.sidebar.header("📊 Dashboard Filters")

# Multi-select for Participants
participants = sorted(df['Participant_Code'].unique())
chosen_pts = st.sidebar.multiselect(
    "Select Energy Providers", 
    options=participants, 
    default=participants[:3]
)

# Slider for Year
# We use the min and max of the Year column we just created
chosen_years = st.sidebar.slider(
    "Select Year Range", 
    int(df['Year'].min()), 
    int(df['Year'].max()), 
    (2016, 2017)
)

# 4. Apply Filters
mask = (df['Participant_Code'].isin(chosen_pts)) & (df['Year'].between(chosen_years[0], chosen_years[1]))
f_df = df[mask]

# 5. Dashboard Display
st.title("⚡ AEMR Market Reliability Command Center")

# Create the 2x2 layout
r1c1, r1c2 = st.columns(2)
r2c1, r2c2 = st.columns(2)

# Chart 1: Bar
with r1c1:
    st.plotly_chart(px.bar(f_df, x='Outage_Reason', y='Energy_Lost_MW', color='Outage_Reason', title="Impact by Category"), use_container_width=True)

# Chart 2: Line
with r1c2:
    t_df = f_df.groupby(['Year', 'Month']).size().reset_index(name='Count')
    t_df['Date'] = pd.to_datetime(t_df[['Year', 'Month']].assign(DAY=1))
    st.plotly_chart(px.line(t_df, x='Date', y='Count', markers=True, title="Outage Trend"), use_container_width=True)

# Chart 3: Scatter
with r2c1:
    st.plotly_chart(px.scatter(f_df, x='Outage_Time_Hours', y='Energy_Lost_MW', color='Risk_Classification', marginal_x="histogram", title="Duration vs Impact"), use_container_width=True)

# Chart 4: Treemap
with r2c2:
    st.plotly_chart(px.treemap(f_df, path=['Participant_Code', 'Outage_Reason'], values='Energy_Lost_MW', title="Market Share Breakdown"), use_container_width=True)