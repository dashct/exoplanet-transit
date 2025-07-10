from lightkurve import search_targetpixelfile

tpf = search_targetpixelfile('Kepler-10', author='Kepler', cadence='long', quarter=4).download()
lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)

lc.plot()

adjusted_lc = lc.flatten()
adjusted_lc.plot()