from typing import List
from sympy import exp, pi, sqrt
from sympy.physics.optics.polarization import stokes_vector
from sympy.physics.optics.gaussopt import BeamParameter
from sympy.physics.quantum.constants import hbar
from sympy.matrices.repmatrix import MutableRepMatrix

c = 300000000  # speed of light

class Beam:
    parameter: BeamParameter
    polarization: MutableRepMatrix
    power: float
    duration: float

    def __init__(self, parameter, power=1, polarization=stokes_vector(0, 0, 0)):
        self.parameter = parameter
        self.polarization = polarization
        self.power = power

    def __eq__(this, other):
        return (
            this.parameter == other.parameter
            and this.polarization == other.polarization
            and this.power == other.power
        )

    def disc_mask(self, D: float, d: float) -> float:
        """_summary_: Calculates the fraction of beam projected in a disc

        Args:
            d (float): length of optical path
            D (float): diameter of receiver opening
        """
        return (1 + exp(-(D / self.gaussianSpotSize(d))**2 / 2))

    def number_of_photons(self):
        return self.duration * self.power * self.parameter.wavelen / (2 * pi * hbar * c)

    def photon_fraction_in_disc(self, D: float, d: float):
        return self.number_of_photons() * self.disc_mask(D, d)

    def gaussianSpotSize() -> float:
        pass


class DataStream:
    """Data beam having a beam power, wavelength and divergence"""

    data: List[Beam]

    def __init__(self, data) -> None:
        self.data = data
