# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:38:36 2015

@author: A
"""
import numpy as np
import math


def euclidean(a, b):
    dist = ((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5
    return(dist)


def opt_euclidean(a, b):
    dist = math.sqrt(pow((b[0]-a[0]), 2) + pow((b[1]-a[1]), 2))
    return(dist)


def np_euclidean(a, b):
    #   dist = np.euclidean(a, b)
    dist = np.sqrt(np.pow((b[0]-a[0]), 2) + np.pow((b[1]-a[1]), 2))
    return(dist)

#    a = [2, 3]
#    b = [5, 6]
#    print(euclidean(a, b))
#    print(opt_euclidean(a, b))
