import pandas as pd
import matplotlib.pyplot as plt

def render_geographic_nodes():
    """
    Surgical rendering of NPA wealth distribution using 
    virtual geometry nodes (EPSG:4326).
    """
    data = {
        'NPA': ['213/310/323', '415/628', '650', '408/669', '949/714', '619/858', '916'],
        'Region': ['Los Angeles', 'San Francisco', 'Silicon Valley South', 'San Jose', 'Orange County', 'San Diego', 'Sacramento'],
        'Lat': [34.05, 37.77, 37.44, 37.33, 33.68, 32.71, 38.58],
        'Lon': [-118.24, -122.41, -122.14, -121.88, -117.86, -117.16, -121.49],
        'Income_Index': [85, 98, 95, 92, 88, 82, 75]
    }
    
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 12), facecolor='white')
    
    plt.scatter(df['Lon'], df['Lat'], s=df['Income_Index']*15, c=df['Income_Index'], 
                cmap='YlOrRd', edgecolor='black', linewidth=1.5, alpha=0.9)

    for i, txt in enumerate(df['Region']):
        plt.annotate(txt, (df['Lon'][i]+0.1, df['Lat'][i]), fontsize=9, weight='bold')

    plt.title("California: NPA Wealth Distribution Node Map", fontsize=16, pad=20)
    plt.savefig('income_heatmap_v2.png', dpi=300, bbox_inches='tight')
    print("[+] Map rendered successfully.")

if __name__ == "__main__":
    render_geographic_nodes()
