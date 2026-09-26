import numpy as np
from gedqd_exchange.core import anticrossing_gap_uev, exchange_superexchange_uev

def test_zero_detuning_gap():
    assert np.isclose(anticrossing_gap_uev(0,5),10)

def test_exchange_positive():
    assert exchange_superexchange_uev(5,1000)>0
