# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:48:51 2020

@author: Pratiksha
"""

def nextPowerOf2(n): 
    count = 0; 
    if (n and not(n & (n - 1))): 
        return n 
    while( n != 0): 
        n >>= 1
        count += 1
    return 1 << count; 

def andProduct(a, b):
    x=a & ~(nextPowerOf2(a^b)-1)
    return x

a,b=map(int,input('Enter the range : ').split())
result=andProduct(a,b)
print('Result of bitwise and of a range :',result)