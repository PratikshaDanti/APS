# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:43:07 2020

@author: Pratiksha
"""

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input('Enter the number : '))
p=fib(n)
print(n,'th fibonacci in sequence is ',p)