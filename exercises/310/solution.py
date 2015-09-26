# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:20:32 2015

@author: A
"""
# with open("words") as myfile:
f = open("words", 'r')
t = f.readlines()
j = len(t)
u = 0
for line in range(0, j):
    # print(t[line], "", line)
    if "e" in t[line]:
        u = u + t[line].count("e")
        # print(line, "" , u, end="")
print(u)
f.closed
