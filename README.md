# GeDQD-Exchange-Simulator

GeDQD-Exchange-Simulator is a compact research codebase for modeling **tunnel coupling, charge hybridization, and exchange interactions in germanium double quantum dots**.

The project focuses on transparent low-energy models that can be analyzed quickly and compared against more detailed electrostatic or many-body simulations.

The main physics chain is

[
	ext{detuning}
ightarrow
	ext{charge hybridization}
ightarrow
	ext{singlet energy}
ightarrow
J
ightarrow
	ext{exchange frequency}
ightarrow
	ext{noise sensitivity}.
]

---

## 1. Scientific motivation

Exchange coupling is central to many semiconductor two-qubit gates.

In a double quantum dot, the exchange energy

[
J = E_T-E_S
]

depends on quantities such as:

- interdot tunnel coupling (t_c),
- detuning (epsilon),
- charging energy (U),
- orbital structure,
- gate voltages,
- magnetic field,
- confinement geometry.

Because (J) can vary rapidly with detuning and barrier voltage, exchange gates can also be sensitive to charge noise.

This repository provides simple models for studying that tradeoff.

---

## 2. Current models

The project currently contains two related descriptions.

### 2.1 Two-level anticrossing model

For a simple two-state system,

[
H
=
egin{pmatrix}
epsilon/2 & t_c\
t_c & -epsilon/2
end{pmatrix}.
]

The eigenenergies are

[
E_pm
=
pm
sqrt{
(epsilon/2)^2+t_c^2
}.
]

At zero detuning, the anticrossing gap is

[
Delta = 2t_c.
]

This model is useful for understanding tunnel coupling and avoided crossings.

### 2.2 Three-state singlet Hubbard model

A minimal singlet-sector basis is

[
|S(1,1)angle,
quad
|S(2,0)angle,
quad
|S(0,2)angle.
]

The implemented Hamiltonian is

[
H_S
=
egin{pmatrix}
0 & sqrt{2}t_c & sqrt{2}t_c\
sqrt{2}t_c & U+epsilon & 0\
sqrt{2}t_c & 0 & U-epsilon
end{pmatrix}.
]

The triplet reference energy is taken as zero in the current convention.

If the lowest singlet eigenvalue is (E_S),

[
J=-E_S.
]

This model captures virtual charge admixture that produces exchange.

---

## 3. Perturbative superexchange

Far from charge degeneracy and for sufficiently small tunnel coupling,

[
J
approx
rac{4t_c^2U}
{U^2-epsilon^2}.
]

At zero detuning,

[
J
approx
rac{4t_c^2}{U}.
]

The repository includes both the exact diagonalization and this perturbative expression so they can be compared directly.

---

## 4. Current capabilities

The package provides:

- anticrossing eigenenergies,
- anticrossing gap,
- perturbative exchange,
- exact singlet-sector diagonalization,
- exact exchange energy,
- singlet ground-state wavefunction,
- double-occupancy probability,
- derivative with respect to detuning,
- derivative with respect to tunnel coupling,
- exchange-energy to frequency conversion.

---

## 5. Repository structure

```text
GeDQD-Exchange-Simulator/
├── README.md
├── pyproject.toml
├── examples/
│   ├── dqd_scan.py
│   └── exchange_sweetspot_demo.py
├── src/
│   └── gedqd_exchange/
│       ├── __init__.py
│       ├── core.py
│       ├── hubbard.py
│       └── sensitivity.py
├── tests/
│   ├── test_core.py
│   └── test_hubbard.py
└── .github/
    └── workflows/
        └── tests.yml
```

---

## 6. Installation

```bash
git clone https://github.com/premathul/GeDQD-Exchange-Simulator.git
cd GeDQD-Exchange-Simulator
python -m pip install -e .
```

Development installation:

```bash
python -m pip install -e .[dev]
pytest -q
```

---

## 7. Example: anticrossing

```python
from gedqd_exchange.core import anticrossing_gap_uev

gap = anticrossing_gap_uev(
    detuning_uev=0.0,
    tunnel_uev=8.0,
)

print(gap)
```

At zero detuning this returns approximately

[
2t_c.
]

---

## 8. Example: exact exchange

```python
from gedqd_exchange.hubbard import exchange_exact_uev

J = exchange_exact_uev(
    detuning_uev=0.0,
    tunnel_uev=10.0,
    U_uev=1000.0,
)

print(J)
```

---

## 9. Charge admixture

The singlet ground state can be expressed schematically as

[
|psi_Sangle
=
a|S(1,1)angle
+
b|S(2,0)angle
+
c|S(0,2)angle.
]

The implemented double-occupancy probability is

[
P_{m double}
=
|b|^2+|c|^2.
]

This quantity is useful because stronger charge admixture often increases exchange while also increasing susceptibility to electrical noise.

---

## 10. Exchange sensitivity

The repository numerically evaluates quantities such as

[
rac{partial J}{partialepsilon}
]

and

[
rac{partial J}{partial t_c}.
]

A detuning sweet spot satisfies approximately

[
rac{partial J}{partialepsilon}=0.
]

For the symmetric model, zero detuning is such a point.

That does not imply complete immunity to charge noise because barrier noise can still modify (t_c).

---

## 11. Exchange frequency

Exchange energy can be converted to a characteristic frequency using

[
f_J=rac{J}{h}.
]

This is useful for estimating the natural timescale associated with exchange-mediated operations.

The code reports frequencies in hertz.

---

## 12. Validation

Current tests include:

- zero-detuning anticrossing gap equals (2t_c),
- exchange remains positive in the intended regime,
- exact Hubbard exchange approaches perturbative superexchange for small (t_c/U),
- first-order detuning derivative vanishes at the symmetric point,
- double-occupancy probability remains between zero and one.

---

## 13. Model assumptions

The current Hubbard model is deliberately minimal.

It assumes:

- one relevant orbital per dot,
- one charging scale (U),
- symmetric tunnel coupling,
- no valley degree of freedom,
- no explicit excited orbitals,
- no magnetic-field dependence,
- no spin-orbit-induced tunneling phase,
- no interdot Coulomb term,
- no disorder.

These assumptions are useful for method development but must be revisited for quantitative device modeling.

---

## 14. Units

Current conventions:

- detuning: (mumathrm{eV}),
- tunnel coupling: (mumathrm{eV}),
- charging energy: (mumathrm{eV}),
- exchange: (mumathrm{eV}),
- frequency: hertz.

A common source of mistakes is confusing (t_c), (2t_c), (J), and (J/h). The code keeps these as separate quantities.

---

## 15. Planned development

### Near-term

- interdot Coulomb energy,
- asymmetric dot energies,
- charge occupation expectation values,
- gate lever arms,
- explicit voltage-to-detuning conversion,
- barrier-voltage to (t_c) models,
- exchange maps.

### Intermediate

- excited orbital states,
- asymmetric charging energies,
- Zeeman gradients,
- spin-orbit-assisted tunneling,
- effective two-spin Hamiltonians,
- charge-noise propagation into (J).

### Long-term

The desired modeling pipeline is

[
	ext{gate voltages}
ightarrow
epsilon,t_c,U
ightarrow
H_{m DQD}
ightarrow
J
ightarrow
rac{partial J}{partial V_i}
ightarrow
S_J(f)
ightarrow
	ext{two-qubit gate fidelity}.
]

---

## 16. Connection to device simulation

The current package begins at the level of effective parameters.

A higher-fidelity workflow could obtain

- detuning,
- wavefunction overlap,
- tunnel coupling,
- charging energies

from an electrostatic or Schrödinger solver and then pass those quantities to this package.

This separation allows expensive device simulations and fast low-energy modeling to be used together.

---

## 17. Reproducibility checklist

A reported exchange calculation should include:

- Hamiltonian convention,
- basis ordering,
- (t_c),
- (U),
- detuning,
- units,
- derivative step size,
- whether exchange is exact or perturbative,
- code version.

---

## 18. Contributing

Useful contributions include:

- larger Hubbard bases,
- analytical benchmarks,
- noise propagation,
- plotting utilities,
- experimental fitting functions,
- lever-arm models,
- unit tests,
- documentation.

---

## 19. License

MIT License.

---

## 20. Project status

**Status:** active development.

The present code already supports transparent comparison between anticrossing physics, perturbative exchange, exact singlet-sector exchange, charge admixture, and first-order sensitivity. The long-term goal is to turn this into a practical low-energy design and analysis toolkit for Ge double quantum dots.
