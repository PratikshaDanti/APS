# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:29:24 2020

@author: Pratiksha
"""

def complement(n):
    #return -n
    return ~n+1

n=int(input('Enter the number : '))
n=complement(n)
print("2's complement value is : ",n)