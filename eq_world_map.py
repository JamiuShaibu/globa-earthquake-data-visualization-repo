import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
"""
Some times you need to encode your file, especially if you are using a geojson file
you might have to encode it by passing 'encoding="utf8"' to open.
e.g open(filename, encoding="utf8").
"""
filename = 'eq_data_30_day_m1.json'
with open(filename, 'r', encoding="utf8",) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    location_or_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(location_or_title)
print(mags)
# Map the Earthquakes and customize marker sizes and colors.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [mag*5 for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title='Global Earthquakes:\nAnalysed by: Jamiu Shaibu', title_x=0.5)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
