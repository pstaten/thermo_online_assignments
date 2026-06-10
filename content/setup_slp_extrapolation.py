import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

import warnings
warnings.filterwarnings('ignore')

# Function used to set up the map-like subplots without server-side map data.
def plot_background(ax):
    ax.set_xlabel('Longitude (degrees east)')
    ax.set_ylabel('Latitude (degrees north)')
    ax.grid(True, linewidth=0.3, alpha=0.5)
    return ax

# Constants in SI units.
gravity = 9.80665 # m s^-2
Rd = 287.047 # J kg^-1 K^-1
gamma = 0.0065 # K m^-1
density = 1.25 # kg m^-3

# Open the example netCDF data.
with xr.open_dataset('MERRA2.tavg3.20210531.bottom_level_for_slp_extrapolation.nc', engine='scipy', backend_kwargs={'mmap': False}) as raw_ds:
    ds = raw_ds.load()

# Combine 1D latitude and longitudes into a 2D grid of locations.
lon_2d, lat_2d = np.meshgrid(ds['lon'], ds['lat'])

# Pull out the 0000-0300Z average and 1200-1500Z average data.
# THESE ARE THE 0130 AND 1330 VARIABLES THAT GRAD STUDENTS WILL USE.
ml_z_0130 = ds['H'][0][0] # middle-of-layer height in meters
ml_p_0130 = ds['PL'][0][0] # middle-of-layer pressure in pascals
slp_0130 = ds['SLP'][0] # sea level pressure from model output in pascals
ml_t_0130 = ds['T'][0][0] # middle-of-layer temperature in kelvins
ml_z_1330 = ds['H'][1][0] # middle-of-layer height in meters
ml_p_1330 = ds['PL'][1][0] # middle-of-layer pressure in pascals
slp_1330 = ds['SLP'][1] # sea level pressure from model output in pascals
ml_t_1330 = ds['T'][1][0] # middle-of-layer temperature in kelvins

plot_time = ds['time'][0].dt.strftime('%d %B %Y %H:%MZ').item()
ds.close()

# Calculate a daily average from 12-hours-apart values.
# THIS IS THE MODELED SLP THAT YOU WILL PLOT.
slp_avg = ((slp_0130 + slp_1330) / 2.) # sea level pressure from model output

# THESE ARE THE VARIABLES YOU WILL USE FOR YOUR CALCULATIONS.
ml_z_avg = ((ml_z_0130 + ml_z_1330) / 2.) # middle-of-bottommost-layer height in meters
ml_p_avg = ((ml_p_0130 + ml_p_1330) / 2.) # middle-of-bottommost-layer pressure in pascals
ml_t_avg = ((ml_t_0130 + ml_t_1330) / 2.) # middle-of-bottommost-layer temperature in kelvins
