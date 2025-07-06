import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/eq_data_1_day_m1.json"
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, "w", encoding="utf-8") as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, longs, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longs.append(lon)
    lats.append(lat)


#mapeamos los terrenos
data = [Scattergeo(lon=longs, lat=lats)]
my_layout = Layout(title = 'Global.Earthquakes')

fig = { 'data':data, 'layout': my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')

