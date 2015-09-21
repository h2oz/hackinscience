# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:33:36 2015

@author: A
"""
import sys
# import numbers
ee = sys.argv
if len(ee) == 3:
    print(int(ee[1])-int(ee[2]))
else:
    print("usage: python3 solution.py OP1 OP2")
