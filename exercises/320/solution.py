# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:20:32 2015

@author: A
"""
# with open("words") as myfile:
f = open("words", 'r')
t = f.readlines()
j = len(t)
al = 'abcdefghijklmnopqrstuvwxyz'
alp = dict((k, 1) for k in al)
for x in range(len(alp)):
    lettre = list(alp)[x]
    u = 0
    for line in range(0, j):
        # print(t[line], "", line)
        if lettre in t[line]:
            u = u + t[line].count(lettre)
    alp[lettre] = u
    # print(lettre, "", u, end="")
print(alp)
f.closed
