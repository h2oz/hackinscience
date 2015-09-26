# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:20:32 2015

@author: A
"""

with open("words") as myfile:
    for line in myfile:
        # print(line, end="".strip("\r\n"))
        print(line, end="")
myfile.closed
