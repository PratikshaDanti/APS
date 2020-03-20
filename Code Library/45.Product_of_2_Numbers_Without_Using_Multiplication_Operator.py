# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:08:04 2020

@author: Pratiksha
"""

def russianPeasant(a, b):   
    res = 0 
    while (b > 0): 
        if (b & 1): 
            res = res + a 
        a = a << 1
        b = b >> 1      
    return res 

a,b=map(int,input('Enter 2 values : ').split())
result=russianPeasant(a,b)
print('Product is : ',result)