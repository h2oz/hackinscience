# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:54:10 2015

@author: A
"""
import requests
r = requests.get('http://mdk.fr/ip')
try:
    # r.status_code
    # r.headers['content-type']
    # r.encoding
        print((r.text).split('\n', 1)[0])
except:
    print('No internet connectivity')
