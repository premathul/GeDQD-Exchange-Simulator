import numpy as np
from gedqd_exchange.hubbard import exchange_exact_uev, double_occupancy_probability
from gedqd_exchange.core import exchange_superexchange_uev
from gedqd_exchange.sensitivity import exchange_detuning_susceptibility

def test_exact_matches_perturbative_small_t():
    t=1.0; U=1000.0
    exact=exchange_exact_uev(0,t,U)
    approx=exchange_superexchange_uev(t,U,0)
    assert np.isclose(exact,approx,rtol=0.01)

def test_symmetric_detuning_sweet_spot():
    d=exchange_detuning_susceptibility(0,10,1000,step_uev=1e-2)
    assert abs(d)<1e-8

def test_double_occupancy_bounds():
    p=double_occupancy_probability(0,10,1000)
    assert 0<=p<=1
