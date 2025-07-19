import pandas as pd
import folium

# Step 1: Load data
df = pd.read_csv("military_bases.csv")

# Step 2: Create a base map centered globally
map = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB positron")

# Step 3: Add markers for each base
for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Name']} ({row['Country']})\nType: {row['Type']}",
        icon=folium.Icon(color='blue' if row['Type'] == 'Air Force' else
                         'green' if row['Type'] == 'Army' else
                         'red', icon='flag')
    ).add_to(map)

# Step 4: Save to HTML
map.save("military_bases_map.html")
print("Map has been saved as 'military_bases_map.html'")
