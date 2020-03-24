# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:37:20 2020

@author: Pratiksha
"""

import collections
def circularArrayRotation(a, k):
    d = collections.deque(a)
    d.rotate(k)
    for i in d:
        print(i,end=' ')
    
a=list(map(int,input('Enter the array elements : ').split()))
k=int(input('Enter number of rotations : '))
circularArrayRotation(a,k)