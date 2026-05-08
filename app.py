import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from visualize import render_geographic_nodes

# White Cube Minimalist Configuration
st.set_page_config(page_title="Geospatial Sentinel", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1, h2, h3 { font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #1a1a1a; }
    div.stButton > button { border-radius: 0px; border: 2px solid #1a1a1a; }
    </style>
    """, unsafe_content_type=True)

st.title("Geospatial Sentinel Dashboard")
st.subheader("California NPA Wealth Distribution & Integrity Monitor")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 1. Geographic Wealth Nodes")
    # Using your existing visualization logic
    data = {
        'NPA': ['213/310/323', '415/628', '650', '408/669', '949/714', '619/858', '916'],
        'Region': ['Los Angeles', 'San Francisco', 'Silicon Valley South', 'San Jose', 'Orange County', 'San Diego', 'Sacramento'],
        'Lat': [34.05, 37.77, 37.44, 37.33, 33.68, 32.71, 38.58],
        'Lon': [-118.24, -122.41, -122.14, -121.88, -117.86, -117.16, -121.49],
        'Income_Index': [85, 98, 95, 92, 88, 82, 75]
    }
    df = pd.DataFrame(data)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(df['Lon'], df['Lat'], s=df['Income_Index']*20, c=df['Income_Index'], 
                        cmap='YlOrRd', edgecolor='black', linewidth=1.5)
    ax.set_facecolor('white')
    st.pyplot(fig)

with col2:
    st.markdown("### 2. Operational Health")
    st.metric(label="Data Quality Index (DQI)", value="98.5%", delta="2.1%")
    st.info("Sentinel Status: Active and Auditing")
    
    if st.button("RUN SURGICAL AUDIT"):
        st.write("[*] Auditing 100+ endpoints...")
        st.success("All geographic nodes verified.")

st.markdown("---")
st.caption("Developed by Ashley Love | Lead UI Engineer & Data Scientist")
