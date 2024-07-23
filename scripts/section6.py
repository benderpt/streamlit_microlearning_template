import streamlit as st
import pandas as pd
import plotly.express as px

# Data
data = {
    "Year": list(range(2010, 2026)),
    "Data Generated (zetabytes)": [2, 5, 6.5, 9, 12.5, 15.5, 18, 26, 33, 41, 64.2, 79, 97, 120, 147, 181],
    "Change Over Previous Year (zetabytes)": [None, 3, 1.5, 2.5, 3.5, 3, 2.5, 8, 7, 8, 23.2, 14.8, 18, 23, 27, 34],
    "Change Over Previous Year (%)": [None, 150, 30, 38.46, 38.89, 24, 16.13, 44.44, 26.92, 24.24, 56.59, 23.05, 22.78, 23.71, 22.5, 23.13]
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit theme settings
primary_color = st.get_option("theme.primaryColor")
secondary_bg_color = st.get_option("theme.secondaryBackgroundColor")
text_color = st.get_option("theme.textColor")
font = st.get_option("theme.font")

# Filter selection
filter_column = st.selectbox("Select data to display", df.columns[1:])

# Plotting with Plotly
fig = px.line(df, x="Year", y=filter_column, markers=True, title=f"{filter_column} (2010-2025)")

# Update layout to match Streamlit theme
fig.update_traces(line=dict(color=primary_color))
fig.update_layout(
    font=dict(family=font, color=text_color),
    title_font=dict(size=20, family=font, color=text_color),
    xaxis=dict(tickfont=dict(color=text_color), titlefont=dict(color=text_color)),
    yaxis=dict(tickfont=dict(color=text_color), titlefont=dict(color=text_color)),
)

# Show plot in Streamlit
st.plotly_chart(fig)

# Description
st.write("""
Source: [Exploding Topics - Data Generated Per Day](https://explodingtopics.com/blog/data-generated-per-day#region)
""")
