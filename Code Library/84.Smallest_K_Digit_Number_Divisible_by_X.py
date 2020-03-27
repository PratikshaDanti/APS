# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:20:09 2020

@author: Pratiksha
"""

def answer(X, K): 
    MIN = pow(10, K-1) 
    if(MIN%X == 0): 
        return (MIN) 
    else:
        return ((MIN + X) - ((MIN + X) % X)) 

X = int(input('Enter value of x : '))  
K = int(input('Enter value of k : '))
print(answer(X, K))  
