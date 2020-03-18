# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:02:31 2020

@author: Pratiksha
"""

def computeXOR(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n+1
    else:
        return 0
    
n=int(input('Enter the value of n : '))
result = computeXOR(n)
print('XOR from 1 to n is ',result)