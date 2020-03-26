# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:36:59 2020

@author: Pratiksha
"""

def catalan_binary_trees(n):
    c=[]
    c.append(1)
    c.append(1)
    c.append(2)
    for i in range(3,n+1):
        c.append(0)
        for j in range(0,i):
            c[i]+=c[j] * c[(i-1)-j]
    return c[n]

n=int(input('Enter value of n : '))
x=catalan_binary_trees(n)
print('Result :',x)