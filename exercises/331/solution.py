# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:31:49 2015

@author: A
"""
import json
# from pprint import pprint


def load_json(path):
    f = open(path, 'r', encoding="utf-8")
    # d = f.readlines()
    d = json.load(f)
    f.close()
    # d = dict(zip(d[0::2], d[1::2]))
    # pprint(d)
    return(d)


def test_int(inp):
    try:
        return(int(inp))
    except:
        return(False)


d = load_json("velib.json")
# print(len(d))
for i in range(len(d)):
    # print(d[i]['address'])
    l = d[i]['address'].split()
    m = d[i]['name'].lstrip()
    # print(d[i])
    for j in range(len(l), -1, -1):
        if(test_int(l[j-1])):
            # print(l[j-1:j+4])
            # print(l[j+(5):len(l)])
            d[i]['zip_code'] = l[j-1]
            d[i]['city'] = " ".join(l[j:len(l)])
            d[i]['address'] = (" ".join(l[0:j-1])).split(' -')[0]
            break
    for k in range(len(m)):
        if(test_int(m[k])):
            # print(l[j-1:j+4])
            # print(l[j+(5):len(l)])
            d[i]['name'] = m[k+7:len(m)].lstrip()
            # print(m)
            break
        # break
    # d[i].pop('name')
    # print(d[i])
g = open("solution.json", 'w')
json.dump(d, g)
g.close()
# print(((d[i]['address'].split('- ', 1))[1]).split())
