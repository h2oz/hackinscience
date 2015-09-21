# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:33:36 2015

@author: A
"""
import sys
ee = sys.argv
# if ee:
print(ee)
print(len(ee))
if len(ee) == 2:
    print(sys.argv[1])
else:
    print("usage: python3 solution.py PARAM")
