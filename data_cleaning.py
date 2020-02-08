#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:07:01 2020

@author: balthasar
"""
import json
from data_clean_conversion import conversion
from pathlib import Path



idict = {}

# with open("whats-cooking-kernels-only/train.json") as f:
    d = json.load(f)

# make a dictionary {ingredient: count} of total ingredient mentions in all recipes
for rec in d:
    for i in rec["ingredients"]:
        if i in idict:
            idict[i] += 1
        else:
            idict[i] = 1

idict = {k: v for k, v in sorted(idict.items(), key=lambda item: item[1])}

# convert synonymous ingredients to same name, e.g. wheat flour & plain flour -> flour
for rec in d:
    for i in rec["ingredients"]:
        if i in conversion:
            rec["ingredients"] = conversion[i]

Path("./cleaned").mkdir(parents=True, exist_ok=True)

with open("cleaned/train.json", "w") as f:
    json.dump(d, f)
    
    
