import numpy as np
# from .LineLists import Lines, get_line_wavelength
from astropy.constants import c


class Component:
    _next_id = 0

    def __init__(self, ComponentName="None"):
        self.id = Component._next_id
        Component._next_id += 1
        self.ComponentName = ComponentName
        self.ComponentType = "baseType"
        self.parnames = []
        self.parvalues = []
        self.parlimits = []
        self.parNumber = 0

    def setpar(self, parvalues):
        self.parvalues = parvalues

    def calc(self, waves, parvalues=None):
        return None


class Gaussian(Component):
    def __init__(self, line, ComponentName="None", parvalues=None, parlimits=None):
        Component.__init__(self, ComponentName)
        self.ComponentType = "Gaussian"
        self.parnames = ["flux", "shift", "fwhm"]
        if parvalues is not None:
            self.parvalues = parvalues
        else:
            self.parvalues = [1.0, 0.0, 1.0]
        if parlimits is not None:
            self.parlimits = parlimits
        else:
            self.parlimits = [[0.0, 1.0e6], [-1.0e6, 1.0e6], [0.0, 1.0e6]]
        if isinstance(line, str):
            self.line = get_line_wavelength(line)
        elif isinstance(line, (int, float)):
            self.line = line
        elif isinstance(line, Lines):
            self.line = line.value
        else:
            raise ValueError("line must be a string, Lines, int, or float.")

    def calc(self, waves, parvalues=None):
        """get the Gaussian line profile

        Args:
            waves (numpy.ndarray): the wavelength array
            parvalues ([flux, shift, fwhm], optional): 
                The parameters of the Gaussian profile, in which shift and 
                fwhm are in units of km/s. Defaults to None.

        Returns:
            numpy.ndarray: 
        """
        if parvalues is not None:
            self.parvalues = parvalues
        flux, shift, fwhm = self.parvalues
        sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
        sigma_wave = sigma * 1000 / c.value * self.line
        shift_wave = shift * 1000 / c.value * self.line
        w0 = self.line + shift_wave
        return flux / (sigma_wave * np.sqrt(2 * np.pi)) * np.exp(
            -0.5 * ((waves - w0) / sigma_wave) ** 2
        )


class Dgaussian(Component):
    pass


class Lorentzian(Component):
    pass


class PowerLaw(Component):
    pass


class DPowerLaw(Component):
    pass


class BalmerContinuum(Component):
    pass