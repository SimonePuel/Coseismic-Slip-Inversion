# FEniCS and hIPPYlib Installations via Anaconda


The FEniCS library can be installed in different ways (from source, on Docker, Ubuntu, Anaconda). We suggest to install it via [Anaconda](https://docs.anaconda.com/anaconda/install/index.html). 

[FEniCS](https://fenicsproject.org/download/)-2019.1.0 can be installed on Anaconda by following the instructions on the fenicsproject 
website (https://fenicsproject.org/download/). To install FEniCS via Anaconda run following command on the terminal:

``conda create -n fenicsproject -c conda-forge fenics numpy matplotlib scipy jupyter``

which will create an environment called fenicsproject, containing fenics, numpy, matplotlib, scipy, and jupyter.


The [hIPPYlib](https://hippylib.github.io)-3.0.0 library depends on FEniCS version 2019.1. FEniCS needs to be built with the following dependecies enabled:

* numpy, scipy, matplotlib, mpi4py;
* PETSc and petsc4py (version 3.10.0 or above);
* SLEPc and slepc4py (version 3.10.0 or above);
* PETSc dependencies: parmetis, scotch, suitesparse, superlu_dist, ml, hypre;
* (optional): mshr, jupyter.

It can be downloaded from the hIPPYlib website or installed (https://hippylib.readthedocs.io/en/3.0.0/installation.html) directly in the FEniCS Anaconda 
environment using ``pip``. With the supported version of FEniCS and its dependencies installed on your machine, hIPPYlib can be installed via pip as follows:

``pip install hippylib --user``

Otherwise, to pip install the development version of hIPPYlib use the command:

``pip install -e git+https://github.com/hippylib/hippylib.git@master#egg=hippylib``


Finally, to activate the FEniCS-hIPPYlib environment, use the following command:

``conda activate fenicsproject``

After the environment has been activated, we can start working with the notebook. Navigate to the directory containing the notebook and run the command:

``jupyter notebook``

You will see a page in your web browser with the list of available .ipynb files.
