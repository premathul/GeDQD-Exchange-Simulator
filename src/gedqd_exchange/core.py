import numpy as np

def anticrossing_energies(detuning_uev, tunnel_uev):
    """Eigenenergies [ueV] of [[eps/2, tc],[tc,-eps/2]]."""
    e=np.asarray(detuning_uev,float)
    gap=np.sqrt((e/2)**2+tunnel_uev**2)
    return -gap, gap

def anticrossing_gap_uev(detuning_uev, tunnel_uev):
    lo,hi=anticrossing_energies(detuning_uev,tunnel_uev)
    return hi-lo

def exchange_superexchange_uev(tunnel_uev, U_uev, detuning_uev=0.0):
    """Perturbative Hubbard result J=4 t^2 U/(U^2-eps^2)."""
    if U_uev <= 0:
        raise ValueError("U_uev must be positive")
    if abs(detuning_uev) >= U_uev:
        raise ValueError("requires |detuning| < U")
    return 4*tunnel_uev**2*U_uev/(U_uev**2-detuning_uev**2)

def numerical_derivative(fn, x, dx=1e-3):
    if dx <= 0:
        raise ValueError("dx must be positive")
    return (fn(x+dx)-fn(x-dx))/(2*dx)
