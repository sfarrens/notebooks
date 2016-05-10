#  @file functions.py
#
#  TUTORIAL FUNCTIONS
#
#  Functions required for implementing tutorial scripts.
#
#  @author Samuel Farrens
#  @version 1.0
#  @date 2015
#

import numpy
from psf import *


def gradient_descent(image, psf):

    grad_op = operators.StandardPSF(image, psf, data_format='map')
    grad_op.get_spec_rad(tolerance=1e-6, max_iter=10)

    opt = optimisation.ForwardBackward(numpy.ones(image.shape), grad_op,
                                       prox=linear.Identity(),
                                       cost=None)

    return opt.x_final
