# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:31:49 2015

@author: A
"""
import json
# from pprint import pprint


def load_json(path):
    f = open(path, 'r')
    # d = f.readlines()
    f.closed
    d = json.load(f)
    # d = dict(zip(d[0::2], d[1::2]))
    # pprint(d)
    return(d)

# load_jason("example.json")
