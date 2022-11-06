import copy
from typing import List
from sympy import Matrix, simplify, zeros
from sympy.core.numbers import (I, pi)

from sympy.physics.optics.polarization import (mueller_matrix,
    linear_polarizer, half_wave_retarder, quarter_wave_retarder, phase_retarder)

from models.databeam import Beam

# def eom_transfer_matrix():
#     return FlatRefraction(n_eom, n_air) * \
#             FreeSpace(len_eom) * \
#             FlatRefraction(n_air, n_eom)

def telescope_transfer_matrix():
    return 


def pbs_mueller_matrix():
    horizontal_filter = mueller_matrix(linear_polarizer())
    vertical_filter = mueller_matrix(linear_polarizer(pi/2))
    retarder = mueller_matrix(phase_retarder(pi/2, pi))

    pbs_front_face = vertical_filter
    pbs_side_face = retarder * horizontal_filter
    return simplify(Matrix.vstack(pbs_front_face, pbs_side_face))

def eom_mueller_matrix(theta):
    return mueller_matrix(phase_retarder(0, theta))


def alice_optical_path(bit, base):    
    bit_states = [0, pi, pi/2, 3*pi/2] # V, H, L, R
    eom = eom_mueller_matrix(bit_states[base << 1 | bit])
    vertical_polarizer = mueller_matrix(linear_polarizer(pi / 2))
    qwp = mueller_matrix(half_wave_retarder(pi / 8))
    return qwp * eom * qwp * vertical_polarizer


def bob_optical_path(beam: Beam) -> List[Beam]:
    beam_1 = copy.deepcopy(beam)
    beam_1.power = beam_1.power / 2
    
    split_beams_1 = pbs_mueller_matrix() * beam_1.polarization
    
    out_1 = copy.deepcopy(beam_1)
    out_2 = copy.deepcopy(beam_1)

    out_1.polarization = split_beams_1[:4, :]
    out_2.polarization = split_beams_1[4:, :]

    beam_2 = copy.deepcopy(beam)
    beam_2.polarization = mueller_matrix(quarter_wave_retarder(-pi / 4)) * beam_2.polarization
    
    beam_2.power = beam_2.power / 2
    
    split_beams_2 = pbs_mueller_matrix() * beam_2.polarization

    out_3 = copy.deepcopy(beam_2)
    out_4 = copy.deepcopy(beam_2)
    
    out_3.polarization = split_beams_2[:4, :]
    out_4.polarization = split_beams_2[4:, :]
    

    return [out_1, out_2, out_3, out_4]
    