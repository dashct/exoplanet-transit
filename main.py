import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt

PERIOD = np.linspace(0.5, 1, 10000)
R_star = 1.065

search_result = lk.search_lightcurve('Kepler-10', author='Kepler', cadence='long').download_all()
lc = search_result.stitch().flatten().remove_outliers()

bls = lc.to_periodogram(method='bls', period=PERIOD, frequency_factor=500)

planet_period = bls.period_at_max_power
planet_t0 = bls.transit_time_at_max_power

lc_folded = lc.fold(period=planet_period, epoch_time=planet_t0).bin(0.001).scatter()

lc_folded.plot()
lower_line = 1 - 0.00018
upper_line = 1 + 0.00001
plt.axhline(lower_line) # Bottom
plt.axhline(upper_line) # Top
depth = upper_line - lower_line

R_planet = 109 * R_star * np.sqrt(depth)
