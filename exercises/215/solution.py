# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:39:26 2015

@author: A
"""

from prime_n import is_prime
u = 0
for i in range(222281, 222381):
    zz = format(i, 'b')
    u = sum(int(x) for x in zz if x.isdigit())
    if is_prime(u):
        print(i)
