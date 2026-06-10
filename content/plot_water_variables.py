# Open the browser-friendly NetCDF dataset and store it in a variable named "ds".
# This file was converted from the original NAM GRIB2 surface fields.
ds = xr.open_dataset('nam.t00z.awip3d00.tm00.surface.nc', engine='netcdf4').load()

# Read the longitude data into variable "lon_2d".
lon_2d = ds['longitude']

# Read the latitude data into variable "lat_2d".
lat_2d = ds['latitude']

# Read in the specific humidity data (q) into variable "specific_humidity".
specific_humidity = ds['q']

# Read in the air temperature data (T) into variable "air_temp".
air_temp = ds['t']

ds.close()
mixing_ratio = calc_w(specific_humidity)
virt_temp = calc_T_v(air_temp, specific_humidity, epsilon)

# Convert units for plotting. Calculations above used kg/kg and K.
specific_humidity_plot = specific_humidity * 1000.0
mixing_ratio_plot = mixing_ratio * 1000.0
air_temp_plot = air_temp - 273.15
virt_temp_plot = virt_temp - 273.15

# Create the figure and plot background on different axes.
fig, axarr = plt.subplots(nrows=2, ncols=1, figsize=(12, 14), constrained_layout=True)
axlist = axarr.flatten()
for ax in axlist:
    plot_background(ax)

# Upper plot - specific humidity and mixing ratio.
c1a = axlist[0].contour(lon_2d, lat_2d, specific_humidity_plot, [5, 10, 15, 20, 25, 30], colors='black')
c1b = axlist[0].contour(lon_2d, lat_2d, mixing_ratio_plot, [5, 10, 15, 20, 25, 30], colors='red')
cf1 = axlist[0].contourf(lon_2d, lat_2d, mixing_ratio_plot-specific_humidity_plot,
                         [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], cmap='GnBu', zorder=0, extend='both')
axlist[0].clabel(c1a, fontsize=10, inline=1, inline_spacing=1, fmt='%i', rightside_up=True)
axlist[0].clabel(c1b, fontsize=10, inline=1, inline_spacing=1, fmt='%i', rightside_up=True)
cb1 = fig.colorbar(cf1, ax=axlist[0], orientation='horizontal', shrink=0.74, pad=0)
cb1.set_label('g kg$^{-1}$', size='x-large')
axlist[0].set_title('$q$ (black), $w$ (red), and $w-q$ (shading)', fontsize=14)

# Lower plot - surface temperatures.
c2a = axlist[1].contour(lon_2d, lat_2d, air_temp_plot, [10, 20, 30, 40], colors='black')
c2b = axlist[1].contour(lon_2d, lat_2d, virt_temp_plot, [10, 20, 30, 40], colors='blue')
cf2 = axlist[1].contourf(lon_2d, lat_2d, virt_temp_plot-air_temp_plot,
                         [1, 2, 3, 4, 5], cmap='OrRd', zorder=0, extend='both')
axlist[1].clabel(c2a, fontsize=10, inline=1, inline_spacing=1, fmt='%i', rightside_up=True)
axlist[1].clabel(c2b, fontsize=10, inline=1, inline_spacing=1, fmt='%i', rightside_up=True)
cb2 = fig.colorbar(cf2, ax=axlist[1], orientation='horizontal', shrink=0.74, pad=0)
cb2.set_label('$^\circ$C', size='x-large')
axlist[1].set_title('$T$ (black), $T_v$ (blue), and $T_v-T$ (shading)', fontsize=14)

# Set figure title.
plot_time = ds['time'].dt.strftime('%d %B %Y %H:%MZ').item()
fig.suptitle(plot_time, fontsize=18)

# Display the plot.
plt.show()