# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:51:05 2021

@author: 91913
"""

W= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (most_frequent(W))
