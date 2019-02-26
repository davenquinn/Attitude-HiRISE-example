#!/usr/bin/env python

import rasterio
from fiona import collection
from shapely.geometry import shape
from pyproj import Proj, transform
import numpy as N

from attitude.helpers.dem import extract_shape

DEMFILE="data/DEM/MegaBreccia_DEM.tif"
SHAPEFILE="data/Stratified_basement_lines.shp"

# Transform to northeast Syrtis CRS
# (same one in Quinn & Ehlmann 2019)
# Important: adjust for different data; this CRS is only valid
# over a small area of Mars' surface!
# See https://proj4.org/usage/projections.html for help
syrtis = {
    'proj': 'tmerc',
    'lat_0': 17,
    'lon_0': 76.5,
    'k':0.9996,
    'x_0':0,
    'y_0':0,
    'a':3396190,
    'b':3376200,
    'units': 'm',
    'no_defs': True
}

features = []
with rasterio.open(DEMFILE,'r') as dem:
    with collection(SHAPEFILE, 'r') as f:
        # Coordinate system of DEM and features should be defined
        assert dict(dem.crs) == f.crs

        mars2000 = Proj(**dict(dem.crs))
        syrtis = Proj(**syrtis)

        def change_proj(coords):
            return transform(mars2000, syrtis, *coords)

        for feature in f:
            geom = shape(feature['geometry'])
            #import IPython; IPython.embed(); raise
            ex = extract_shape(geom,dem)
            # Transform to a meters-based coordinate system
            transformed = N.array([change_proj(i) for i in ex])
            features.append(transformed)

