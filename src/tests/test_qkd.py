from sympy.physics.optics.polarization import stokes_vector
from sympy.core.numbers import (I, pi)

from sympy.physics.optics.gaussopt import BeamParameter
from src.models.databeam import Beam

from src.main import generate_beam, receive_beam

no_beam = stokes_vector(0, 0, 0, 0)
vertical_polarization = stokes_vector(psi = pi/2, chi=0, p=1)
horizontal_polarization = stokes_vector(psi = 0, chi=0, p=1)
left_circular_polarization = stokes_vector(psi = 0, chi=-pi/4, p=1)
right_circular_polarization = stokes_vector(psi = pi/2, chi=pi/4, p=1)

v_beam = Beam(parameter=BeamParameter(830e-9, 0, 1e-3), polarization=vertical_polarization / 2)
h_beam = Beam(parameter=BeamParameter(830e-9, 0, 1e-3), polarization=horizontal_polarization / 2)
l_beam = Beam(parameter=BeamParameter(830e-9, 0, 1e-3), polarization=left_circular_polarization / 2)
r_beam = Beam(parameter=BeamParameter(830e-9, 0, 1e-3), polarization=right_circular_polarization / 2)

def test_generate_beam():
    assert generate_beam(False, False) == v_beam
    assert generate_beam(False, True) == h_beam
    assert generate_beam(True, False) == l_beam
    assert generate_beam(True, True) == r_beam

def test_receive_beam():
    assert receive_beam(v_beam) == (False, False)
    assert receive_beam(h_beam) == (False, True)
    assert receive_beam(l_beam) == (True, False)
    assert receive_beam(r_beam) == (True, True)

