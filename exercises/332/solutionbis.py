# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 11:32:08 2015

@author: A
"""
import json
import folium


def load_json(path):
    f = open(path, 'r')
    # d = f.readlines()
    d = json.load(f)
    f.close()
    # d = dict(zip(d[0::2], d[1::2]))
    # pprint(d)
    return(d)


d = load_json("solution.json")
# print(len(d))
map_osm = folium.Map(location=[48.8529, 2.3493], zoom_start=12)
for i in range(len(d)):
    map_osm.circle_marker(location=[d[i]['latitude'], d[i]['longitude']],
                          radius=100,
                          line_color='#3186cc',
                          fill_color='#3186cc',
                          popup=(d[i]['zip_code'] + " " + d[i]['name'] + " " +
                          str(d[i]['latitude']) + " " + str(d[i]['longitude'])
                          )
                          )
map_osm.create_map(path='velib2.html')
