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
sline = 0
for x in range(len(alp)):
    lettre = list(alp)[x]
    u = 0
    for line in range(0, j):
        # print(t[line], "", line)
        # sline = sline + len(t[line])
        if lettre in t[line]:
            u = u + t[line].count(lettre)
    alp[lettre] = u
    # print(lettre, "", u, end="")
# somme = sum(alp.values())
for line in range(0, j):
    sline = sline + len(t[line])
print(somme, sline)
for x in range(len(alp)):
    lettre = list(alp)[x]
    alp[lettre] = alp[lettre]/sline
    print(lettre+":", "%.2f" % alp[lettre])
f.closed
