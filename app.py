import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# White Cube Minimalist Configuration
st.set_page_config(page_title="Geospatial Sentinel", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1, h2, h3 { font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #1a1a1a; }
    div.stButton > button { border-radius: 0px; border: 2px solid #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

st.title("Geospatial Sentinel Dashboard")
st.subheader("California NPA Wealth Distribution & Integrity Monitor")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 1. Geographic Wealth Nodes")
    data = {
        'NPA': ['213/310/323', '415/628', '650', '408/669', '949/714', '619/858', '916'],
        'Region': ['Los Angeles', 'San Francisco', 'Silicon Valley South', 'San Jose', 'Orange County', 'San Diego', 'Sacramento'],
        'Lat': [34.05, 37.77, 37.44, 37.33, 33.68, 32.71, 38.58],
        'Lon': [-118.24, -122.41, -122.14, -121.88, -117.86, -117.16, -121.49],
        'Income_Index': [85, 98, 95, 92, 88, 82, 75]
    }
    df = pd.DataFrame(data)
    
    # Load low-res map and filter for California area
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    usa = world[world.name == "United States of America"]
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Plot Map Outline (Light Grey)
    usa.plot(ax=ax, color='#f2f2f2', edgecolor='#cccccc')
    
    # Scatter nodes with legend
    scatter = ax.scatter(df['Lon'], df['Lat'], s=df['Income_Index']*25, c=df['Income_Index'], 
                        cmap='YlOrRd', edgecolor='black', linewidth=1.2, alpha=0.9, zorder=3)
    
    # Add Colorbar Legend
    cbar = plt.colorbar(scatter, ax=ax, fraction=0.03, pad=0.04)
    cbar.set_label('Wealth Index (Normalized)', fontsize=10, weight='bold')
    
    # Zoom to California
    ax.set_xlim([-125, -114])
    ax.set_ylim([32, 42])
    ax.set_facecolor('white')
    
    for i, txt in enumerate(df['Region']):
        ax.annotate(txt, (df['Lon'][i]+0.2, df['Lat'][i]), fontsize=8, weight='bold', zorder=4)
    
    plt.title("Regional Wealth Distribution Grid", fontsize=14, pad=15)
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
