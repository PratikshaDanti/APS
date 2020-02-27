# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:48:38 2020

@author: Pratiksha
"""

n=int(input('Enter the nth number in sequence : '))
memo=[]
memo.append(0)
memo.append(1)
for i in range(2,n):
    memo.append(memo[i-1]+memo[i-2])
    
print('Memoization table values: ',memo)
print('Fibonacci of nth number is : ',memo[n-1])