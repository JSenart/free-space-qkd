from sympy import Matrix
from sympy.physics.optics.polarization import stokes_vector
from sympy.core.numbers import (I, pi)

from .context import qkd

from sympy.physics.optics.polarization import (mueller_matrix, quarter_wave_retarder)

no_beam = stokes_vector(0, 0, 0, 0)
horizontal_polarization = stokes_vector(psi = 0, chi=0, p=1)
vertical_polarization = stokes_vector(psi = pi/2, chi=0, p=1)
left_circular_polarization = stokes_vector(psi = 0, chi=-pi/4, p=1)
right_circular_polarization = stokes_vector(psi = pi/2, chi=pi/4, p=1)

def test_pbs():
    assert qkd.optical_setup.pbs_mueller_matrix() * horizontal_polarization == Matrix.vstack(no_beam, horizontal_polarization)
    assert qkd.optical_setup.pbs_mueller_matrix() * vertical_polarization == Matrix.vstack(vertical_polarization, no_beam)
    assert qkd.optical_setup.pbs_mueller_matrix() * left_circular_polarization == Matrix.vstack(vertical_polarization / 2, horizontal_polarization / 2)
    assert qkd.optical_setup.pbs_mueller_matrix() * right_circular_polarization == Matrix.vstack(vertical_polarization / 2, horizontal_polarization / 2)

def test_qwp():
    qwp = mueller_matrix(quarter_wave_retarder(pi / 4))
    assert qwp * horizontal_polarization == right_circular_polarization
    assert qwp * right_circular_polarization == vertical_polarization
    assert qwp * vertical_polarization == left_circular_polarization
    assert qwp * left_circular_polarization == horizontal_polarization

if __name__=='__main__':
    test_pbs()
    test_qwp()