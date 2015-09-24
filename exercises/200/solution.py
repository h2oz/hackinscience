# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:39:26 2015

@author: A
"""


def is_prime(num):
    if(num == 0 or num == 1):
        return False
    for i in range(2, num):
        if(i != num):
            if(num % i == 0):
                # print(num, i, num % i)
                return False
    return True

#    print(is_prime(0))
#    print(is_prime(1))
#    print(is_prime(113))
