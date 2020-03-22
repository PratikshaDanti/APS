# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:12:46 2020

@author: Pratiksha

Given a value N, if we want to make change for N cents, and we have infinite supply
of each of S = { S1, S2, .. , Sm} valued coins, 
how many ways can we make the change? The order of coins doesn’t matter.

"""

def count(S, m, n): 
    table = [0 for k in range(n+1)] 
    table[0] = 1
    for i in range(0,m): 
        for j in range(S[i],n+1): 
            table[j] += table[j-S[i]] 
  
    return table[n] 
  
arr = list(map(int,input('Enter denominations : ').split())) 
m = len(arr) 
n = int(input('Enter the value : '))
x = count(arr, m, n) 
print(x) 
  