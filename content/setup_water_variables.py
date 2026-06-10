# These import lines open up software that makes Python
# more able to do science and display the results.
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

import warnings
warnings.filterwarnings('ignore')

# The NAM file uses longitudes in degrees east.
PLOT_EXTENT = [235., 290., 20., 55.]

# Function used to set up the map-like subplots without server-side map data.
def plot_background(ax):
    ax.set_xlim(PLOT_EXTENT[0], PLOT_EXTENT[1])
    ax.set_ylim(PLOT_EXTENT[2], PLOT_EXTENT[3])
    ax.set_xlabel('Longitude (degrees east)')
    ax.set_ylabel('Latitude (degrees north)')
    ax.grid(True, linewidth=0.3, alpha=0.5)
    return ax

"""
If you are new to coding functions, the comments in this code below will help you.
"""

# def is short for "define." This next line defines a function called "calc_epsilon." It operates on two inputs, R_d and R_v.
def calc_epsilon(R_d, R_v):
    # Notice that the next few lines of code are indented?
    # These indented lines are 'inside' calc_epsilon.
    
    # "Return" means that this function spits out an answer.
    # In this case, the answer it spits out is R_d/R_v.
    return R_d/R_v

# The code is no longer indented.
# We are no longer 'inside' calc_epsilon.

R_dry_air = 287.05 # g kg^-1 K^-1
R_water_vapor = 461.52 # g kg^-1 K^-1
epsilon = calc_epsilon(R_dry_air, R_water_vapor)

