from typing import List
import numpy as np
from sympy.physics.optics.polarization import stokes_vector
from sympy.physics.optics.gaussopt import BeamParameter
from sympy.matrices.repmatrix import MutableRepMatrix


class Beam:
    parameter: BeamParameter
    polarization: MutableRepMatrix
    power: float

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

    def powerInDisc(self, r: float, d: float) -> float:
        return self.power * (1 + np.exp(-2 * np.square(r / self.gaussianSpotSize(d))))

    def gaussianSpotSize(d: float) -> float:
        pass


class DataStream:
    """Data beam having a beam power, wavelength and divergence"""

    data: List[Beam]

    def __init__(self, data) -> None:
        self.data = data
