from sympy import exp, pi, sqrt
from sympy.physics.quantum.constants import hbar

from qkd.models.databeam import Beam

# TODO: Adicionar weather conditions
# TODO: Encontrar dados (na tese do vladlen en referencias) de condicoes atmosfericas na barragem do alqueva

orbital_height = 500000  # Chosen orbit height in meters

c = 300000000  # speed of light

p_0 = 1  # Initial Power
w_d = 1  # Gaussian Spot Size
mu_q = 1  # Quantum Efficiency
mu_opt = 1  # Optical Efficiency
eta = mu_q * mu_opt
delta_t = 10  #  time between key exchanges

y_0 = 0  # Dark count probability
e_det = 0  # Basis misalignment
std_dev = 0.1  # Standard deviation of Gaussian White noise

photon_wavelength = 850e-9  # m
photon_energy = (
    2 * pi * hbar * c / photon_wavelength
)  # photon energy for photon of wavelength gama


def quantum_bit_error_rate(theta):
    tmp = 1 - exp(-eta * sc_gs_distance(theta) * generalized_loss(theta))
    return (y_0 / 2 + e_det * tmp) / (y_0 / 2 + tmp)


def sifted_key_rate(
    received_beams: list[Beam],
    emitted_key: list[bool],
    received_key: list[bool],
    gaussian_noise: list[float],
    d: float,
    D: float,
):
    key_sum = sum(
        rb.photon_fraction_in_disc(d, D) * exp(-((x / std_dev) ** 2) / 2)
        for a, b, x, rb in zip(emitted_key, received_key, gaussian_noise, received_beams)
        if a == b
    )
    return key_sum / (std_dev * len(emitted_key) * sqrt(2*pi))


def sc_gs_distance(theta):
    return orbital_height


def generalized_loss(theta):
    return 1
