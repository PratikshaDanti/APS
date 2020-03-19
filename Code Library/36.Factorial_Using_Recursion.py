# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:40:16 2020

@author: Pratiksha
"""
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input('Enter the number : '))
p=factorial(n)
print('Factorial of ',n,' is ',p)
