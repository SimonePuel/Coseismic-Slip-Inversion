# Coseismic Slip Inversion

This repository contains finite-element (FE) models of earthquake problems using the open-source libraries [FEniCS](https://fenicsproject.org) and [hIPPYlib](https://hippylib.github.io) for the forward and inverse problems, respectively. In particular, the goal is to invert surface displacement data for the coseismic slip distribution using adjoint-based optimization methods and a mixed FE elastic formulation.


1) [FEniCS](https://fenicsproject.org) (Logg_Wells, 2010; Logg et al., 2012) is a high-level parallel FE collection of software components for automated and efficient solution of PDEs. It includes several libraries for the FE discretization, assembly and solution of linear and non-linear systems of equations. In FEniCS, any PDE can be explicitly and easily expressed in variational form using the *Unified Form Language* (Alnaes et al., 2014) Python library. This makes a problem coded in this framework transparent, reproducible, flexible for multi-physics formulations, and easy to implement. 


2) [hIPPYlib](https://hippylib.github.io) (Villa et al., 2016; Villa et al., 2018; Villa et al., 2021) implements state-of-the-art scalable adjoint-based algorithms for PDE-based deterministic and Bayesian inverse problems. In hIPPYlib, derivative information, gradients and actions of the second derivative of objective functions (Hessian), are efficiently computed using the adjoint method while leveraging the automated symbolic differentiation and assembly of variational forms in FEniCS.


### Installation of the FEniCS and hIPPYlib libraries

For the installation of the two open-source libraries and all their dependeciens, please look at the file ``FEniCS_hIPPYlib_installation.md``.


### Mesh Generation and Visualization

For models with complex geometries, the open-source mesh geration software, [Gmsh](https://www.gmsh.info/) (Geuzaine & Remacle, 2009), can be used to create the mesh which is then imported to FEniCS.

[Matplotlib](https://matplotlib.org) and [Paraview](https://www.paraview.org/) can be used to visualize the results in 2D and 3D, repsectively.


### Jupyer notebooks of GJI manuscript

In the folder ``Manuscript_GJI_2022`` there are the Jupyter notebook tutorials and the files to reproduce the results contained in the manuscript titled "***A Mixed, Unified Forward/Inverse Framework for Earthquake Problems: Fault Implementation and Coseismic Slip Estimate***" submitted to Geophysical Journal International (GJI) by Puel et al. (2022).


### Copyright and distribution

All the material contained in this repository is open-source and can be distributed under the GNU General Public License v3.0. 


If you have any questions/suggestions or you are simply interested in this forward-inverse FE framework, please constact Simone Puel (spuel@utexas.edu).
