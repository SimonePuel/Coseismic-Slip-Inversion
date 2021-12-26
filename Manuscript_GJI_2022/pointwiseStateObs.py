# Copyright (c) 2016-2018, The University of Texas at Austin
# & University of California, Merced.
#
# All Rights reserved.
# See file COPYRIGHT for details.
#
# This file is part of the hIPPYlib library. For more information and source code
# availability see https://hippylib.github.io.
#
# hIPPYlib is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License (as published by the Free
# Software Foundation) version 2.0 dated June 1991.


import dolfin as dl
import hippylib as hp


class PointwiseStateObservation(hp.Misfit):
    """
    This class implements pointwise state observations at given locations.
    It assumes that the state variable is a scalar function.
    """
    def __init__(self, Vh, obs_points, indicator_vec=None):
        """
        Constructor:

            :code:`Vh` is the finite element space for the state variable

            :code:`obs_points` is a 2D array number of points by geometric dimensions that stores \
            the location of the observations.

            :code:`indicator_vec`: vector that allows you to select what part of the state you want to use in your misfit \
            when working with a mixed problem (or a problem whose state has multiple fields).
        """
        if indicator_vec is not None:
            B = hp.assemblePointwiseObservation(Vh, obs_points)
            self.B = DomainRestrictedOperator(indicator_vec, B)
        else:
            self.B = hp.assemblePointwiseObservation(Vh, obs_points)

        self.d = dl.Vector(self.B.mpi_comm())
        self.B.init_vector(self.d, 0)
        self.Bu = dl.Vector(self.B.mpi_comm())
        self.B.init_vector(self.Bu, 0)
        self.noise_variance = None

    def cost(self,x):
        if self.noise_variance is None:
            raise ValueError("Noise Variance must be specified")
        elif self.noise_variance == 0:
            raise  ZeroDivisionError("Noise Variance must not be 0.0 Set to 1.0 for deterministic inverse problems")
        self.B.mult(x[hp.STATE], self.Bu)
        self.Bu.axpy(-1., self.d)
        return (.5/self.noise_variance)*self.Bu.inner(self.Bu)

    def grad(self, i, x, out):
        if self.noise_variance is None:
            raise ValueError("Noise Variance must be specified")
        elif self.noise_variance == 0:
            raise  ZeroDivisionError("Noise Variance must not be 0.0 Set to 1.0 for deterministic inverse problems")
        if i == hp.STATE:
            self.B.mult(x[hp.STATE], self.Bu)
            self.Bu.axpy(-1., self.d)
            self.B.transpmult(self.Bu, out)
            out *= (1./self.noise_variance)
        elif i == hp.PARAMETER:
            out.zero()
        else:
            raise IndexError()

    def setLinearizationPoint(self,x, gauss_newton_approx=False):
        # The cost functional is already quadratic. Nothing to be done here
        return

    def apply_ij(self,i,j,dir,out):
        if self.noise_variance is None:
            raise ValueError("Noise Variance must be specified")
        elif self.noise_variance == 0:
            raise  ZeroDivisionError("Noise Variance must not be 0.0 Set to 1.0 for deterministic inverse problems")
        if i == hp.STATE and j == hp.STATE:
            self.B.mult(dir, self.Bu)
            self.B.transpmult(self.Bu, out)
            out *= (1./self.noise_variance)
        else:
            out.zero()



class DomainRestrictedOperator:
    """
    This class defines a linear operator that zeros out fields in the state vector.
    """
    def __init__(self, indicator_vec, B):
        """
        Constructor:

            :code:`indicator_vec`: vector that allows you to select what part of the state you want to zero out\
            when working with a mixed problem (or a problem whose state has multiple fields).

            :code:`B` is a PETSc matrix that projects the state onto the location of observations.
        """
        self.indicator_vec = indicator_vec
        self.B = B

    def mpi_comm(self):
        return self.B.mpi_comm()

    def init_vector(self, v, dim):
        return self.B.init_vector(v, dim)

    def mult(self, u, y):
        self.B.mult(u*self.indicator_vec, y)

    def transpmult(self, y, u):
        self.B.transpmult(y, u)
        u *= self.indicator_vec
