# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:39:26 2015

@author: A
"""

from prime_n import is_prime
u = 0
for i in range(1000):
    if is_prime(i):
        u = u + i
print(u)
