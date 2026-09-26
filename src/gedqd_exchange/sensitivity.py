import numpy as np
from .hubbard import exchange_exact_uev

def derivative(fn, x, dx):
    if dx<=0: raise ValueError("dx must be positive")
    return (fn(x+dx)-fn(x-dx))/(2*dx)

def exchange_detuning_susceptibility(detuning_uev, tunnel_uev, U_uev, step_uev=1e-2):
    fn=lambda e: exchange_exact_uev(e,tunnel_uev,U_uev)
    return derivative(fn,detuning_uev,step_uev)

def exchange_tunnel_susceptibility(detuning_uev, tunnel_uev, U_uev, step_uev=1e-3):
    fn=lambda t: exchange_exact_uev(detuning_uev,t,U_uev)
    return derivative(fn,tunnel_uev,step_uev)

def exchange_frequency_hz(exchange_uev):
    return np.asarray(exchange_uev,float)*1e-6/4.135667696e-15
