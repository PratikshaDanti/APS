# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:53:21 2020

@author: Pratiksha
"""

def findUnique(arr):
    out=0
    for i in arr:
        out=i^out
    return out
     
arr=list(map(int,input('Enter the array elements : ').split()))

print(findUnique(arr))