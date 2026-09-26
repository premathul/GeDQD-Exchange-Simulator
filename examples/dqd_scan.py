import numpy as np
from gedqd_exchange.core import anticrossing_gap_uev, exchange_superexchange_uev

tc=8.0
for eps in np.linspace(-100,100,5):
    print(f"eps={eps:7.1f} ueV gap={anticrossing_gap_uev(eps,tc):8.3f} ueV")
print("J(0) =", exchange_superexchange_uev(tc,1000.0), "ueV")
