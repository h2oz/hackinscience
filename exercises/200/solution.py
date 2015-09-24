# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:39:26 2015

@author: A
"""


def is_prime(num):
    for i in range(2, num):
        if(i != num):
            if(num % i == 0):
                # print(num, i, num % i)
                return False
    return True

# print(is_prime(15))
# print(is_prime(11))
# print(is_prime(113))
