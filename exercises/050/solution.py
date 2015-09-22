# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:33:36 2015

@author: A
"""
j = 0
for i in range(1001):
    if (i % 3 == 0) and (i % 5 == 0):
        j = i+j
print(j)
