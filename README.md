# GeDQD-Exchange-Simulator

Minimal numerical tools for exploring tunnel coupling and exchange in a germanium double quantum dot.

## Current model
The first release uses a two-site Hubbard-inspired model with detuning \\(\epsilon\\), tunnel coupling \\(t_c\\), and charging scale \\(U\\).

In the far-detuned perturbative regime, exchange can be approximated from virtual charge admixture. The package also provides a direct two-level anticrossing spectrum to visualize \\(t_c\\).

## Quick start
```bash
python -m pip install -e .
python examples/dqd_scan.py
pytest
```

## Roadmap
- full singlet-sector Hamiltonian
- lever-arm conversion
- charge-noise susceptibility
- barrier-gate response models
- two-qubit gate figures of merit

## Status
Generic research prototype; no unpublished device parameters are included.

## License
MIT.
