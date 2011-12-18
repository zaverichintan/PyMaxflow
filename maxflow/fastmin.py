# -*- coding: utf-8 -*-

"""
maxflow.fastmin
===============

``fastmin`` provides implementations of the algorithms for
fast energy minimization described in [BOYKOV01]_: the alpha-expansion
and the alpha-beta-swap.

.. [BOYKOV01] *Fast approximate energy minimization via graph cuts.*
   Yuri Boykov, Olga Veksler and Ramin Zabih. TPAMI 2001.

Currently, the functions in this module are restricted to
grids with von Neumann neighborhood.
"""

import sys
from itertools import count, combinations
import numpy as np
import _maxflow
from _maxflow import abswap_grid_step, aexpansion_grid_step

def energy_of_grid_labeling(D, V, labels):
    """
    Returns the energy of the labeling of a grid.
    
    For details about ``D``, ``V`` and ``labels``, see the
    documentation of ``aexpansion_grid``.
    
    Returns the energy of the labeling.
    """
    
    num_labels = D.shape[0]
    ndim = labels.ndim
    
    # Sum of the unary terms.
    unary = np.sum([D[i,labels==i].sum() for i in range(num_labels)])
    
    slice0 = [slice(None)]*ndim
    slice1 = [slice(None)]*ndim
    # Binary terms.
    binary = 0
    for i in range(ndim):
        slice0[i] = slice(1, None)
        slice1[i] = slice(None, -1)
        
        binary += V[labels[slice0],labels[slice1]].sum()
        
        slice0[i] = slice(None)
        slice1[i] = slice(None)
    
    return unary + binary

def abswap_grid(D, V, max_cycles, labels=None):
    """
    Minimize an energy function iterating the alpha-beta-swap
    until convergence or until a maximum number of cycles,
    given by ``max_cycles``, is reached.
    
    ``D`` must be a N+1-dimensional array with shape (L,S1,...,SN),
    where L is the number of labels considered. *D[lbl,p1,...,pn]* is the unary
    cost of assigning the label *lbl* to the variable *(p1,...,pn)*.
    
    ``V`` is a two-dimensional array. *V[lbl1,lbl2]* is the binary cost of
    assigning the labels *lbl1* and *lbl2* to a pair of neighbor variables.
    Note that the abswap algorithm, unlike the aexpansion, does not require
    ``V`` to define a metric.
    
    The optional N-dimensional array ``labels`` gives the initial labeling
    for the algorithm. If not given, the function uses a plain initialization
    with all the labels set to 0.
    
    This function return the labeling reached at the end of the algorithm.
    If the user provides the parameter ``labels``, the algorithm will work
    modifying this array in-place.
    """
    raise NotImplementedError, "No disponible para esta práctica"

def aexpansion_grid(D, V, max_cycles=None, labels=None):
    """
    Minimize an energy function iterating the alpha-expansion until
    convergence or until a maximum number of cycles,
    given by ``max_cycles``, is reached.
    
    ``D`` must be an N+1-dimensional array with shape (L,S1,...,SN),
    where L is the number of labels considered. *D[lbl,p1,...,pn]* is the unary
    cost of assigning the label *lbl* to the variable *(p1,...,pn)*.
    
    ``V`` is a two-dimensional array. *V[lbl1,lbl2]* is the binary cost of
    assigning the labels *lbl1* and *lbl2* to a pair of neighbor variables.
    Note that the distance defined by ``V`` must be a metric or the aexpansion
    might fail.
    
    The optional N-dimensional array ``labels`` gives the initial labeling
    of the algorithm. If not given, the function uses a plain initialization
    with all the labels set to 0.
    
    This function return the labeling reached at the end of the algorithm.
    If the user provides the parameter ``labels``, the algorithm will work
    modifying this array in-place.
    """
    raise NotImplementedError, "No disponible para esta práctica"

