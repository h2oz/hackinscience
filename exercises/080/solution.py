# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:33:36 2015

@author: A
"""
al = 'abcdefghijklmnopqrstuvwxyz'
ll = len(al)
for ii in range(ll):
    for jj in range(ii, ll):
        if (jj != ii):
            print(al[ii]+al[jj])
