# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:31:33 2020

@author: Pratiksha
"""

from itertools import permutations
s=str(input('Enter the string : '))
l=[]
for i in range(1,len(s)+1):
    p=list(permutations(s,i))
    for j in p:
        x=''
        for k in range(len(j)):
            x=x+j[k]
        if x not in l:
            if len(set(x))==len(x):
                l.append(x)
print(l)