# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#this code intends to run a batch processing list of algorithms of all the files sentinel files in the folder 

#	open folder
# Easiest done using the python library 'glob'
# https://docs.python.org/3/library/glob.html
from glob import glob
import os    # All the operating system commands to break up paths and file names

"""
glob needs the full path to the image files
I suggest to get the path as a command line arguement
So this script will be called as "sentinel_code.py <path/to/images>
If no path is given, then the default will be the current working dir

***********************************
TODO for Tamir
    Prepare a test to check for the command line argument
    check out: sys.argv
    https://docs.python.org/3/library/sys.html?highlight=argv#module-sys
    If it exists, set the variable 's2_path' to that path for glob
    If it doesn't exist set s2_path = "./"
    hint: len(sys.argv) > 0
***********************************
"""

s2_list = glob(os.path.join(s2_path, "*.SAFE"))
# Are we working with the raw "*.SAFE" compressed format?
# or extracted *.tif ??

#	make and input the list of files in folder in list 

for s2_file in s2_list:
    s2_name = os.path.splitext(os.path.split(s2_file)[1])[0]
    """
    ***********************************
    TODO for Tamir:
        Why do I need the subset index [1] and [0] above ?
    ***********************************
    """
#	break file names into details: date, sensor, product etc etc
    s2_file_components = "_".split(s2_name)
    # Now we have:
    # s2_file_components[0] is the mission
    # s2_file_components[1] is the level
    # s2_file_components[2] is the acquisition date string
    # s2_file_components[3] is the processing number
    # s2_file_components[4] is the orbit number
    # s2_file_components[5] is the tile number

#	open additional files: shp file for clipping
    """
    ***********************************
    TODO for Tamir:
        Convert the date string to an actual python date object
        Hint: see the strptime function in datetime module
        https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.datetime.strptime
    ***********************************
    """





##########	loop through list	###############

#	open file 

#	optional: convert epsg to utm or israel 2039

#	stck all layers (resample spatially) https://gis.stackexchange.com/questions/80620/using-gdal-python-to-stack-georeferenced-images-of-different-sizes

#	clip layer cy shp file
# POLYGON ((34.00929260253906 31.324234008789062, 34.01079559326172 31.324234008789062, 34.01079559326172 31.347789764404297, 34.00929260253906 31.347789764404297, 34.00929260253906 31.324234008789062, 34.00929260253906 31.324234008789062))

#	designate names to layers







##########	calculate indices:  NDVI etc	#################

#	NDVI = (NIR — VIS)/(NIR + VIS)
