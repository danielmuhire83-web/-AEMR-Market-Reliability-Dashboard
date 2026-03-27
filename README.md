⚡ AEMR Market Reliability Dashboard

Master of Applied Data Science (MADS) - Independent Learning Project
This repository contains an interactive data science application built to analyze energy grid stability for the Australian Energy Market Regulator (AEMR). The project demonstrates a transition from SQL-based data extraction to advanced Python-based visualization and web deployment.

🔗 Live Application
View the Live Dashboard here:http://localhost:8501/

📊 Project Overview

The goal of this dashboard is to provide a "Single-Screen Command Center" for monitoring power outages. It allows users to:
Identify Magnitude: See which outage reasons (Forced vs. Scheduled) cause the most energy loss.
Track Trends: Observe monthly fluctuations in grid reliability over 2016-2017.
Analyze Correlation: Evaluate the relationship between outage duration and total energy impact.
Assess Market Share: Visualize the hierarchical impact of specific market participants.

🛠️ Tech Stack

Dashboard Framework: Streamlit (Procedural logic)
Visualization Library: Plotly Express (Declarative syntax)
Data Manipulation: Pandas
Deployment: GitHub & Streamlit Community Cloud

📈 Key Visualizations

Bar Chart: Total Energy Lost (MW) by Outage Reason.
Line Chart: Monthly Outage Frequency Trend.
Scatter Plot: Duration (Hours) vs. Energy Lost with Marginal Histograms.
Treemap: Hierarchical breakdown of Participant Impact and Outage Causes.

🧹 Data Engineering

The project involved cleaning raw AEMR CSV data, including:
Handling invalid date strings (e.g., September 31st).
Engineering a custom Outage_Time_Hours feature using timedelta operations.
Managing missing values in risk classification tiers.



