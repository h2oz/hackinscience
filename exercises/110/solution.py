# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:07:59 2015

@author: A
"""

import sys
import operator


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

zz = sys.argv
ops = ({"+": operator.add, "-": operator.sub, "*": operator.mul,
       "/": operator.truediv, "%": operator.mod, "^": operator.pow})
if(len(zz) != 4):
    print("input error")
    print(len(zz))
if(is_int(zz[1]) and (type(zz[2]) is str) and
   is_int(zz[3])):
    print(ops[zz[2]](int(zz[1]), int(zz[3])))
# for i in range(len(zz)):
#    print(type(zz[i]))
