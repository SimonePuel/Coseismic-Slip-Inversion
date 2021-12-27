# FEniCS-hIPPYlib framework

This repository contains finite-element (FE) models of earthquake problems using the open-source libraries, [FEniCS](https://fenicsproject.org) and [hIPPYlib](https://hippylib.github.io) for the forward and inverse problems, respectively.

[FEniCS](https://fenicsproject.org) (Logg_Wells, 2010; Logg et al., 2012) is a high-level parallel FE collection of software components for automated and efficient solution of PDEs. It includes several libraries for the FE discretization, assembly and solution of linear and non-linear systems of equations.

In FEniCS, any PDE can be explicitly and easily expressed in variational form using the *Unified Form Language* (Alnaes et al., 2014) Python library. This makes a problem coded in this framework transparent, reproducible, flexible for multi-physics formulations, and easy to implement. 

[hIPPYlib](https://hippylib.github.io) (Villa et al., 2016, Villa et al., 2018, Villa et al., 2021) implements state-of-the-art scalable adjoint-based algorithms for PDE-based deterministic and Bayesian inverse problems.

In hIPPYlib, derivative information, gradients and actions of the second derivative of objective functions (Hessian), are efficiently computed using the adjoint method while leveraging the automated symbolic differentiation and assembly of variational forms in FEniCS.

For models with complex geometries, [Gmsh](https://www.gmsh.info/) can be used to create the mesh, which is then imported to FEniCS.

[Matplotlib](https://matplotlib.org) and [Paraview](https://www.paraview.org/) can be used to visualize the results in 2D and 3D, repsectively.
