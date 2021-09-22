from arcgis.gis import GIS

my_gis = GIS()
m = my_gis.map()
m.save({'title': 'Italy streets', 'snippet': 'Arterial road network of Italy', 'tags': 'streets, network, roads'})
