import colour
import matplotlib.pyplot as plt
data = {
    400: 0.0300,
    500: 0.0651,
    520: 0.0705,
    540: 0.0772,
    560: 0.0870,
    580: 0.1128,
    590: 0.1200,
    600: 0.1360,
    850: 0.2000
}
sd = colour.SpectralDistribution(data)

print(f"spectral density at wave length 550.5nm is {sd[550.5]}")
print(f"first 3 elements of the data is {sd[0:2]}")
print(f"shape of this is {repr(sd.shape)} which includes wavelength {sd.shape.wavelengths}")

illuminant = colour.SDS_ILLUMINANTS["D65"]
print("------")

# this code from 
# https://colour.readthedocs.io/en/v0.3.7/_modules/colour/colorimetry/blackbody.html#blackbody_spd

DEFAULT_SPECTRAL_SHAPE = colour.colorimetry.spectrum.SpectralShape(450, 850, 10)
C1 = 3.741771e-16  # 2 * math.pi * PLANCK_CONSTANT * LIGHT_SPEED ** 2
C2 = 1.4388e-2  # PLANCK_CONSTANT * LIGHT_SPEED / BOLTZMANN_CONSTANT
N = 1

def blackbody_spd(temperature,
                  shape=DEFAULT_SPECTRAL_SHAPE,
                  c1=C1,
                  c2=C2,
                  n=N):
    """
    Returns the spectral power distribution of the planckian radiator for given
    temperature :math:`T[K]`.

    Parameters
    ----------
    temperature : numeric
        Temperature :math:`T[K]` in kelvin degrees.
    shape : SpectralShape, optional
        Spectral shape used to create the spectral power distribution of the
        planckian radiator.
    c1 : numeric, optional
        The official value of :math:`c1` is provided by the Committee on Data
        for Science and Technology (CODATA), and is
        :math:`c1=3,741771x10.16\ W/m_2` (Mohr and Taylor, 2000).
    c2 : numeric, optional
        Since :math:`T` is measured on the International Temperature Scale,
        the value of :math:`c2` used in colorimetry should follow that adopted
        in the current International Temperature Scale (ITS-90)
        (Preston-Thomas, 1990; Mielenz et aI., 1991), namely
        :math:`c2=1,4388x10.2\ m/K`.
    n : numeric, optional
        Medium index of refraction. For dry air at 15°C and 101 325 Pa,
        containing 0,03 percent by volume of carbon dioxide, it is
        approximately 1,00028 throughout the visible region although
        CIE 15:2004 recommends using :math:`n=1`.

    Returns
    -------
    SpectralPowerDistribution
        Blackbody spectral power distribution.

    Examples
    --------
    >>> from colour import STANDARD_OBSERVERS_CMFS
    >>> cmfs = STANDARD_OBSERVERS_CMFS.get(
    ...     'CIE 1931 2 Degree Standard Observer')
    >>> blackbody_spd(5000, cmfs.shape)  # doctest: +ELLIPSIS
    <colour.colorimetry.spectrum.SpectralPowerDistribution object at 0x...>
    """

    wavelengths = shape.range()
    return colour.colorimetry.spectrum.SpectralDistribution(
        name='{0}K Blackbody'.format(temperature),
        data=dict(
            zip(wavelengths,
                colour.colorimetry.planck_law(
                    wavelengths * 1e-9, temperature, c1, c2, n))))

sd5000k = blackbody_spd(5000, sd.shape)
#fig, ax = colour.plotting.plot_multi_sds([sd, sd5000k])
plt.figure(facecolor="yellow")
fig, ax = colour.plotting.plot_single_sd(sd5000k)
ax.set_facecolor("gray")
fig.set_facecolor("pink")
fig.savefig("hoge2.png")
