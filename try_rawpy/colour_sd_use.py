import colour

data = {
    500: 0.0651,
    520: 0.0705,
    540: 0.0772,
    560: 0.0870,
    580: 0.1128,
    590: 0.1200,
    600: 0.1360,
}
sd = colour.SpectralDistribution(data)

print(f"spectral density at wave length 550.5nm is {sd[550.5]}")
print(f"first 3 elements of the data is {sd[0:2]}")
print(f"shape of this is {repr(sd.shape)} which includes wavelength {sd.shape.wavelengths}")

illuminant = colour.SDS_ILLUMINANTS["D65"]
fig, ax = colour.plotting.plot_single_sd(sd)
