# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:53:45 2015

@author: A
"""

import json
import math


def load_json(path):
    f = open(path, 'r', encoding="utf-8")
    # d = f.readlines()
    d = json.load(f)
    f.close()
    # d = dict(zip(d[0::2], d[1::2]))
    # pprint(d)
    return(d)


def opt_euclidean(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    return math.hypot(x, y)


def locate(lat, long):
    k = 0
    d = load_json("solution.json")
    a = [lat, long]
    for i in range(0, len(d)):
        b_old = [d[k]['latitude'], d[k]['longitude']]
        b_new = [d[i]['latitude'], d[i]['longitude']]
        d[i]['distance'] = opt_euclidean(a, b_new)
        if (opt_euclidean(a, b_new) <= opt_euclidean(a, b_old)):
            k = i
    print(d[k])
    return()


# locate(48.8645278209524, 2.416170724425902)
