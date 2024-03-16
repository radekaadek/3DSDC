from owslib.wfs import WebFeatureService
import pandas as pd
import numpy as np
import os
import sys
import shapely
import geopandas as gpd
import rasterio

sys.path.append("../cw1")
import pobierz_dane

def get_sample_aoi_bounds() -> shapely.Polygon:
    aoi_bounds = [566894.9, 244146.1, 567550.6, 244605.2]
    aoi_polygon = shapely.Polygon.from_bounds(*aoi_bounds)
    return aoi_polygon

wfs_service_url = "https://mapy.geoportal.gov.pl/wss/service/PZGIK/NumerycznyModelTerenuEVRF2007/WFS/Skorowidze"
wfs_service = WebFeatureService(wfs_service_url, version="2.0.0")
bounds = (566894.9, 244146.1, 567550.6, 244605.2)
# print layers
layers = list(wfs_service.contents)
# ['SkorowidzNMPT2019', 'SkorowidzNMPT2020', 'SkorowidzNMPT2021', 'SkorowidzNMPT2022', 'SkorowidzNMPT2023']
response = wfs_service.getfeature(typename=layers[-1], bbox=bounds)

with open("dane.xml", "wb") as f:
    f.write(response.read())

sections = gpd.read_file("dane.xml")
# check if directory exists
# if not os.path.exists("./dane"):
#     os.mkdir("./dane")
# for url_do_pobierania in sections["url_do_pobrania"]:
#     pobierz_dane.download_and_save_file(url_do_pobierania, f"./dane/{url_do_pobierania.split('/')[-1]}.asc")

aoi = shapely.Polygon()
features = gpd.GeoDataFrame()
features["nazwa"] = ["a" for _ in range(100)]
features["wartosc"] = [np.random.rand() for _ in range(100)]

# filter features wartosc > 0.5
features = features[features["wartosc"] > 0.5]


