# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:24:41 2020

@author: Pratiksha
"""

def answer(X, K): 
    MAX = pow(10, K) - 1
    return (MAX - (MAX % X)) 
  
X = int(input('Enter value of x : '))  
K = int(input('Enter value of k : '))  
print(answer(X, K))  
