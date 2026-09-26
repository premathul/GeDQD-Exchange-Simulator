# GeDQD-Exchange-Simulator

GeDQD-Exchange-Simulator is a research software project for studying tunnel coupling, charge hybridization, and exchange interactions in germanium double quantum dots. The repository focuses on low-energy models that are simple enough to inspect analytically but rich enough to reproduce the essential physics of avoided crossings, singlet charge admixture, and electrically controlled exchange. The aim is to provide a clear bridge between device-level quantities such as detuning and tunnel coupling and qubit-level quantities such as exchange frequency, charge-noise susceptibility, and two-qubit interaction strength.

In semiconductor double quantum dots, exchange arises because the singlet and triplet states do not respond identically to virtual tunneling into doubly occupied charge configurations. When tunneling is allowed, the singlet state can hybridize with ((2,0)) and ((0,2)) charge states, while the triplet is restricted by Pauli exclusion in a minimal single-orbital model. This lowers the singlet energy relative to the triplet and generates an exchange splitting

[
J=E_T-E_S.
]

Because the amount of virtual charge admixture depends strongly on detuning and tunnel coupling, exchange can be controlled electrically. That electrical tunability is one of the major advantages of semiconductor two-qubit gates, but it also creates a direct pathway for charge noise to affect the interaction.

The repository currently implements two complementary models. The first is a simple two-level anticrossing Hamiltonian,

[
H=
egin{pmatrix}
epsilon/2 & t_c\
t_c & -epsilon/2
end{pmatrix},
]

where (epsilon) is the detuning and (t_c) is the tunnel coupling. The eigenenergies are

[
E_pm=
pmsqrt{(epsilon/2)^2+t_c^2}.
]

At zero detuning, the level separation is (2t_c). This model is useful for understanding the meaning of tunnel coupling and for visualizing avoided crossings without introducing the full spin and charge basis.

The second model is a three-state singlet-sector Hubbard description using the basis

[
|S(1,1)angle,qquad
|S(2,0)angle,qquad
|S(0,2)angle.
]

The implemented Hamiltonian is

[
H_S=
egin{pmatrix}
0 & sqrt{2}t_c & sqrt{2}t_c\
sqrt{2}t_c & U+epsilon & 0\
sqrt{2}t_c & 0 & U-epsilon
end{pmatrix},
]

where (U) is the charging energy. The triplet energy is taken as the zero of energy in the current convention. The exchange energy is then obtained by diagonalizing the singlet Hamiltonian and evaluating

[
J=-E_{S,mathrm{ground}}.
]

This exact diagonalization can be compared with the perturbative superexchange expression

[
Japprox
rac{4t_c^2U}
{U^2-epsilon^2},
]

which reduces at zero detuning to

[
Japproxrac{4t_c^2}{U}.
]

The perturbative result is expected to be accurate only when the charge states remain well separated in energy and (t_c/U) is small. The repository includes tests that verify the exact model approaches the perturbative result in the appropriate regime.

An important output of the Hubbard model is the charge composition of the singlet ground state. If

[
|psi_Sangle=
a|S(1,1)angle+
b|S(2,0)angle+
c|S(0,2)angle,
]

then the total double-occupancy probability is

[
P_{mathrm{double}}=
|b|^2+|c|^2.
]

This quantity is physically useful because it measures how strongly the nominal ((1,1)) spin state mixes with charge states. In many exchange-gate scenarios, increasing charge admixture increases the available interaction strength while also increasing exposure to electrical noise. The repository is intended to help explore that tradeoff quantitatively.

The code also evaluates numerical derivatives such as

[
rac{partial J}{partialepsilon}
]

and

[
rac{partial J}{partial t_c}.
]

These derivatives provide a first-order measure of how exchange responds to detuning noise and barrier-control noise. In the symmetric model, the point (epsilon=0) is a first-order detuning sweet spot because the exchange curve is locally even in detuning and therefore

[
left.
rac{partial J}{partialepsilon}
ight|_{epsilon=0}
=0.
]

This does not mean that the qubit is completely immune to charge noise. Fluctuations in the tunnel barrier can still modify (t_c), and higher-order detuning sensitivity can remain important.

Exchange energy can be converted into an interaction frequency using

[
f_J=rac{J}{h}.
]

The distinction between (t_c), the anticrossing gap (2t_c), the exchange energy (J), and the exchange frequency (J/h) is maintained explicitly throughout the code because confusing these quantities can easily produce order-of-two or unit errors.

The repository is organized into small modules. The `core.py` file contains the simple two-state anticrossing model and perturbative exchange expression. The `hubbard.py` file contains the three-state singlet Hamiltonian, diagonalization, exact exchange, and charge-admixture analysis. The `sensitivity.py` file contains numerical derivatives and exchange-frequency conversion. Example scripts demonstrate detuning sweeps and exchange sweet spots, while the tests verify analytical limits and physical constraints.

Installation can be performed with

```bash
git clone https://github.com/premathul/GeDQD-Exchange-Simulator.git
cd GeDQD-Exchange-Simulator
python -m pip install -e .
```

For development and testing,

```bash
python -m pip install -e .[dev]
pytest -q
```

A minimal exchange calculation can be written as

```python
from gedqd_exchange.hubbard import exchange_exact_uev

J = exchange_exact_uev(
    detuning_uev=0.0,
    tunnel_uev=10.0,
    U_uev=1000.0,
)

print(J)
```

The numerical parameters in examples are generic and are not intended to reproduce a particular fabricated device.

The present model is deliberately minimal. It assumes one relevant orbital per dot, a single charging scale, symmetric tunnel coupling, and no explicit interdot Coulomb term. It does not include excited orbitals, spin-orbit-dependent tunnel phases, Zeeman gradients, valley degrees of freedom, disorder, magnetic-field dependence of the orbital wavefunctions, or realistic electrostatic lever arms. These omissions matter when moving from qualitative physics to quantitative modeling.

A natural next step is to connect the effective parameters (epsilon), (t_c), and (U) to actual gate voltages. In experiment, detuning is often written approximately as a lever-arm-weighted voltage combination, while tunnel coupling depends nonlinearly on barrier-gate voltage. Once these relations are included, the code can calculate derivatives such as

[
rac{partial J}{partial V_i},
]

which are directly relevant to charge-noise-induced fluctuations of the two-qubit interaction.

A further extension is to include additional charge and orbital states. In realistic Ge double dots, excited orbitals, asymmetry between the two dots, spin-orbit coupling, and magnetic-field direction can all influence exchange. The long-term goal is not to construct an enormous many-body solver inside this repository, but to retain a compact low-energy representation whose parameters can be extracted from a higher-fidelity device calculation.

That higher-fidelity interface is important. A realistic workflow could use an electrostatic or Schrödinger solver to obtain orbital energies and wavefunction overlap, infer an effective tunnel coupling and charging energy, and then pass those quantities to this repository for fast parameter sweeps and noise analysis. In that sense, GeDQD-Exchange-Simulator is intended to serve as the low-energy interaction layer of a larger simulation ecosystem.

The long-term modeling chain is

[
	ext{gate voltages}
ightarrow
epsilon,t_c,U
ightarrow
H_{mathrm{DQD}}
ightarrow
J
ightarrow
rac{partial J}{partial V_i}
ightarrow
S_J(f)
ightarrow
	ext{exchange-gate performance}.
]

Future work will include explicit lever arms, asymmetric dots, interdot Coulomb interaction, larger Hubbard bases, charge occupation maps, exchange-noise propagation, and eventually effective two-spin Hamiltonians suitable for estimating gate times and sensitivity.

Reproducibility requires reporting the Hamiltonian convention, basis ordering, detuning sign convention, (t_c), (U), derivative step size, units, and whether a result is obtained from exact diagonalization or perturbation theory. The code is designed so that these distinctions remain visible.

The repository is currently suitable for analytical cross-checks, parameter studies, graduate research training, and rapid exploration of exchange physics. Publication-level device predictions will require calibration of the effective parameters against experiment or a higher-fidelity simulation.

## Contact

**Athul Prem**

For questions, collaboration, scientific discussion, or suggestions related to this project, please contact Athul Prem through the GitHub account associated with the repository.
