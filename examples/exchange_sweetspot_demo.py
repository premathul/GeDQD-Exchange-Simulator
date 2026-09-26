import numpy as np
from gedqd_exchange.hubbard import exchange_exact_uev, double_occupancy_probability
from gedqd_exchange.sensitivity import exchange_detuning_susceptibility, exchange_frequency_hz

for eps in np.linspace(-400,400,9):
    J=exchange_exact_uev(eps,10,1000)
    dJ=exchange_detuning_susceptibility(eps,10,1000)
    p=double_occupancy_probability(eps,10,1000)
    print(f"eps={eps:7.1f} ueV J={J:8.4f} ueV fJ={exchange_frequency_hz(J)/1e6:8.3f} MHz dJ/deps={dJ:9.5f} Pdouble={p:.5f}")
