# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:06:04 2020

@author: Pratiksha
"""

def isPowerOfTwo(x):
    return(x and (not(x & (x - 1))))

n=int(input('Enter the number : '))
print(isPowerOfTwo(n))