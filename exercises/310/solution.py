# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:20:32 2015

@author: A
"""
# with open("words") as myfile:
f = open("words", 'r')
# t = f.readlines()
# u = t.count("e")
u = 0
for line in f:
    if "e" in line:
        u += 1
print(u)
f.closed
