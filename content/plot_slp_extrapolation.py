# The pressure values are already in pascals for calculations.

# Convert Pa to hPa for plotting.
ml_p_avg_plot = ml_p_avg / 100.0
slp_avg_plot = slp_avg / 100.0
slp_const_temp_avg_plot = slp_const_temp_avg / 100.0
slp_const_gamma_avg_plot = slp_const_gamma_avg / 100.0

# Create the figure and plot background on different axes.
fig, axarr = plt.subplots(nrows=2, ncols=2, figsize=(14, 8), constrained_layout=True)
axlist = axarr.flatten()
for ax in axlist:
    plot_background(ax)

ps_levs = [500, 600, 700, 800, 900, 1000, 1100]
slp_levs = [970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060]

# Upper left plot - near-surface pressure.
cf1 = axlist[0].contourf(lon_2d, lat_2d, ml_p_avg_plot, cmap='gist_earth_r', levels=ps_levs, extend='both', zorder=0)
axlist[0].set_title('Near-surface pressure', fontsize=14)
cb1 = fig.colorbar(cf1, ax=axlist[0], orientation='horizontal', shrink=0.74, pad=0)
cb1.set_label('hPa', size='large')

# Upper right plot - modeled sea level pressure.
cf2 = axlist[1].contourf(lon_2d, lat_2d, slp_avg_plot, cmap='RdBu_r', levels=slp_levs, extend='both', zorder=0)
axlist[1].set_title('Modeled sea-level pressure', fontsize=14)
cb2 = fig.colorbar(cf2, ax=axlist[1], orientation='horizontal', shrink=0.74, pad=0)
cb2.set_label('hPa', size='large')

# Lower left plot - calculated sea level pressure, constant temperature.
cf3 = axlist[2].contourf(lon_2d, lat_2d, slp_const_temp_avg_plot, cmap='RdBu_r', levels=slp_levs, extend='both', zorder=0)
axlist[2].set_title(r'Calculated sea-level pressure, $\overline{T}$', fontsize=14)
cb3 = fig.colorbar(cf3, ax=axlist[2], orientation='horizontal', shrink=0.74, pad=0)
cb3.set_label('hPa', size='large')

# Lower right plot - calculated sea level pressure, constant lapse rate.
cf4 = axlist[3].contourf(lon_2d, lat_2d, slp_const_gamma_avg_plot, cmap='RdBu_r', levels=slp_levs, extend='both', zorder=0)
axlist[3].set_title(r'Calculated sea-level pressure, $\overline{\Gamma}$', fontsize=14)
cb4 = fig.colorbar(cf4, ax=axlist[3], orientation='horizontal', shrink=0.74, pad=0)
cb4.set_label('hPa', size='large')

# Set figure title.
fig.suptitle(plot_time, fontsize=18)

# Display the plot.
plt.show()
