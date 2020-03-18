# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:30:16 2020

@author: Pratiksha
"""

def swap(a,b):
    a ^= b
    b ^= a 
    a ^= b
    return a,b
a,b=map(int,input('Enter the numbers : ').split())
print("values before swapping : ",a,b)
a,b=swap(a,b)
print("values after swapping : ",a,b)
