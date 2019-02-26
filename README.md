# Attitude: basic usage example

This is a basic usage example for the `attitude`
Python module on HiRISE DEM data and imagery of
NE Syrtis megabreccia.

The images and shapefiles
should be put in the `data/` directory, and the model
is contained in the Python and IPython notebook
files in the main directory.

## Installation

First (optionally) create a virtual environment
to hold the installed python modules. At the command line:

```
export PROJECT_DIR=$(pwd)
source setup-environment.sh
```

Then, install the required python modules:
```
pip install -r requirements.txt
```

Finally, open the Jupyter notebook (you may need to separately install Jupyter
or download Nteract if you don't already have them installed), and run all the
cells. You should see a visualization of the orientations.

## Modifying for new data

This project is adaptable to different elevation datasets and their matching
extracted shapefiles. Several changes need to be made:

1. Paths in `extract_shapes.py` must be adjusted to find the new data
2. DEMs and shapefiles should have matching geospatial projections
3. The projection information in `extract_shapes.py` should be updated to
   a local coordinate reference system appropriate to your data (*with the
   same horizontal and vertical units*, typically meters). Good examples are
   UTM coordinate reference systems. See [the PROJ.4 documentation](https://proj4.org/usage/projections.html) or [SpatialReference.org](http://spatialreference.org/).
