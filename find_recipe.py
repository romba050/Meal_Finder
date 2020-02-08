#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:47:51 2020

@author: basilerommes
"""

import json

#with open("cleaned/train.json") as f:
with open("whats-cooking-kernels-only/train.json") as f:
    # list of 3 dictionaries: id, cuisine, ingredients
    d_clean = json.load(f)

# matches 24717 pretty well
test_query = ["onions", "spinach", "red lentils", "tumeric", "garam masala", "sweet potatoes"]#["cheese", "bell pepper", "fish"]

def search_by_id(id_int):
    for rec in d_clean:
        if rec["id"] == id_int:
            return rec
        
recipe = search_by_id(24717)
list(set(recipe["ingredients"]).intersection(set(test_query)))

def count_matches(query):
    # {rec_id: count of intersections with query}
    compatibilities = []  # 2-tuple list of (recipe_id, matches) pairs
    for rec in d_clean:
        ingred_matches = len((set(rec["ingredients"]).intersection(set(test_query))))
        #compatibilities[rec["id"]] = len(ingred_matches)
        compatibilities.append((rec["id"], ingred_matches))
    return compatibilities

test_matches = count_matches(test_query)
# sort in descending order
sorted_matches = sorted(test_matches, key=lambda x: x[1], reverse=True)

#max_matches = max(test_matches.values())
# to get the recipe with the most matches: sort after 2nd element, return first element of sorted list
best_fit = sorted_matches[0]  # (id, num_matches) tuple
print(f"Best fit:\n{search_by_id(best_fit[0])}")

    