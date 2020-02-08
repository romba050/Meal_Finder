#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:07:01 2020

@author: balthasar
"""
import json
from data_clean_conversion import conversion


idict = {}

with open("whats-cooking-kernels-only/train.json") as f:
    d = json.load(f)

for rec in d:
    for i in rec["ingredients"]:
        if i in idict:
            idict[i] += 1
        else:
            idict[i] = 1

idict = {k: v for k, v in sorted(idict.items(), key=lambda item: item[1])}

for rec in d:
    for i in rec["ingredients"]:
        if i in conversion:
            rec["ingredients"]

with open("cleaned/train.json", "w") as f:
    json.dump(d, f)