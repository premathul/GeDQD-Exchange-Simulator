import numpy as np

def singlet_hamiltonian_uev(detuning_uev, tunnel_uev, U_uev):
    """Three-state singlet Hamiltonian in basis S(1,1), S(2,0), S(0,2)."""
    if U_uev<=0: raise ValueError("U_uev must be positive")
    eps=float(detuning_uev); t=float(tunnel_uev)
    c=np.sqrt(2.0)*t
    return np.array([[0.0,c,c],[c,U_uev+eps,0.0],[c,0.0,U_uev-eps]],float)

def singlet_spectrum_uev(detuning_uev, tunnel_uev, U_uev):
    return np.linalg.eigvalsh(singlet_hamiltonian_uev(detuning_uev,tunnel_uev,U_uev))

def exchange_exact_uev(detuning_uev, tunnel_uev, U_uev):
    """Exchange J = E_T - E_S with triplet reference E_T=0."""
    e0=singlet_spectrum_uev(detuning_uev,tunnel_uev,U_uev)[0]
    return -float(e0)

def singlet_ground_state(detuning_uev, tunnel_uev, U_uev):
    h=singlet_hamiltonian_uev(detuning_uev,tunnel_uev,U_uev)
    vals,vecs=np.linalg.eigh(h)
    return float(vals[0]),vecs[:,0]

def double_occupancy_probability(detuning_uev, tunnel_uev, U_uev):
    _,psi=singlet_ground_state(detuning_uev,tunnel_uev,U_uev)
    return float(abs(psi[1])**2+abs(psi[2])**2)
