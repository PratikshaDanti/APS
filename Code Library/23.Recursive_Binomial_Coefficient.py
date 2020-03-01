# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:22:13 2020

@author: Pratiksha
"""

def bin_coeff(n,k):
    if n==k or k==0:
        return 1
    else:
        return bin_coeff(n-1,k-1)+bin_coeff(n-1,k)
    
n,k=map(int,input('Enter n and k values : ').split())
x=bin_coeff(n,k)
print(x)