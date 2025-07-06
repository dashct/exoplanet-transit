import lightkurve as lk

# Search for Kepler-10 light curve data
search_result = lk.search_lightcurve('Kepler-10', mission='TESS')

# Download the first available light curve
lc = search_result.download()

# Plot the raw light curve
lc.plot()