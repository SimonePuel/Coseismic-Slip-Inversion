# A Mixed, Unified Forward/Inverse Framework for Earthquake Problems: Fault Implementation and Coseismic Slip

This folder contains the Jupyter notebook tutorials and the files to reproduce the results in the manuscript accepted in Geophysical Journal International (GJI) in 2022 titled:
 
"***A mixed, unified forward/inverse framework for earthquake problems: fault implementation and coseismic slip estimate***"

Authors:
Simone Puel (1,2) (spuel@utexas.edu)
Eldar Khattatov (3)
Umberto Villa (4)
Dunyu Liu (2)
Omar Ghattas (1,3,5)
Thorsten W. Becker (1,2,3)

1) Department of Geological Sciences, Jackson School of Geosciences, The University of Texas at Austin, Austin, TX 78712, USA 
2) Institute for Geophysics, Jackson School of Geosciences, The University of Texas at Austin, Austin, TX 78712, USA 
3) Oden Institute for Computational Engineering and Sciences, The University of Texas at Austin, Austin, TX 78712, USA 
4) Electrical and Systems Engineering, Washington University in St. Louis, St. Louis, MO 63112, USA 
5) Walker Department of Mechanical Engineering, The University of Texas at Austin, Austin, TX 78712, USA

To cite:
*Puel, S., Khattatov, E., Villa, U., Liu, D., U., Ghattas, O., Becker, T. W. (2022). A mixed, unified forward/inverse framework for earthquake problems: fault implementation and coseismic slip estimate. Geophysical Journal International, 230(2), 733–758. https://doi.org/10.1093/gji/ggac050.*


### Description Jupyter notebook files

- ``ManufacturedSolution_ConvergenceRate.ipynb`` - tutorial to compute the comparison and convergence rate analysis between the standard displacement formulation (DF), the mixed finite-element elastic formulation (MF) and the exact solution estimated by using the manufactured solution;
- ``CrackII_ConvergenceRate.ipynb`` - tutorial to compute the comparison and convergence rate analysis of a shear crack mode II between the standard displacement formulation with split-node fault implementation (DF), the mixed finite-element elastic formulation with our new fault implementation (MF) and the analytic solution (Pollard & Segall, 1987); 
- ``CoseismicSlip_DeterministicInversion.ipynb`` - tutorial to compute the deterministic linear inversion of the coseismic slip distribution using our new FEniCS-hIPPYlib framework via adjoint-based optimization methods.
