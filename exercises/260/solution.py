# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:38:36 2015

@author: A
"""
import numpy as np
import math


def euclidean(a, b):
    zz = 0
    for x in range(len(a)):
        zz = zz + (a[x]-b[x])**2
    dist = (zz)**0.5
    return(dist)


def opt_euclidean(a, b):
    zz = 0
    for x in range(len(a)):
        zz = zz + math.pow((a[x]-b[x]), 2)
    dist = math.sqrt(zz)
    return(dist)


def np_euclidean(a, b):
    # pt_1 = np.array((a[0], a[1]))
    # pt_2 = np.array((b[0], b[1]))
    # dist = np.linalg.norm(pt_1-pt_2)
    zz = 0
    for x in range(len(a)):
        zz = zz + np.power((a[x]-b[x]), 2)
    dist = np.sqrt(zz)
    return(float(dist))


#    def np_euclidean2(a, b):
#        x = np.array(a[0], a[1])
#        y = np.array(b[0], b[1])
#        return np.linalg.norm(x - y)

#    a = [2, 3, 7, 3, 4, 0, 8, 2, 1]
#    b = [5, 3, 0, 7, 8, 6, 9, 4, 5]
#    a = [2, 3]
#    b = [5, 6]
#    print(euclidean(a, b))
#    print(opt_euclidean(a, b))
#    print(np_euclidean(a, b))
#    print(np_euclidean2(a, b))
#    print(euclidean(a, b) == opt_euclidean(a, b) == np_euclidean(a, b))
