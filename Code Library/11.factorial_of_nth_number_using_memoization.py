# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:48:38 2020

@author: Pratiksha
"""

n=int(input('Enter the number : '))
memo=[]
memo.append(1)
memo.append(1)
for i in range(2,n+1):
    memo.append(i*memo[i-1])
    
print('Memoization table values: ',memo)
print('Factorial of ',n,' is : ',memo[n])