# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:38:36 2015

@author: A
"""
import numpy as np
import math


def euclidean(a, b):
    return ((b[0]-a[0]) ** 2 + (b[1]-a[1]) ** 2) ** 0.5


def opt_euclidean(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    return math.hypot(x, y)


def np_euclidean(a, b):
    x = np.array(a[0], a[1])
    y = np.array(b[0], b[1])
    return np.linalg.norm(x - y)
