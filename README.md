# Thermo Weeks 5 and 6

Two browser-friendly Jupyter notebook labs for atmospheric thermodynamics students:

- `week5_water_vapor_variables_[lastname]_[firstname].ipynb`
- `week6_slp_extrapolation_[lastname]_[firstname].ipynb`

The notebooks have been adapted to run in JupyterLite or a lightweight local Jupyter environment. They avoid Docker-specific dependencies and do not require `cfgrib`, `ecCodes`, `MetPy`, `Cartopy`, or `latexify-py`.

## Data files

- `nam.t00z.awip3d00.tm00.surface.nc` is a small NetCDF file converted from the original NAM GRIB2 file. It contains only the surface temperature and specific humidity fields needed for the Week 5 lab.
- `MERRA2.tavg3.20210531.bottom_level_for_week_6.nc4` is used directly by the Week 6 lab.
- `nam.t00z.awip3d00.tm00.grib2` is the original Week 5 source file and is no longer required by the revised notebook.

## Runtime packages

The notebooks use:

- `matplotlib`
- `netCDF4`
- `numpy`
- `xarray`

In JupyterLite, the first import cell tries to install these Pyodide packages into the browser kernel with `piplite`. In a normal conda/Jupyter environment, use `environment.yml`.
