# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:32:26 2020

@author: Pratiksha
"""

def count(S, m, n): 
    table = [0 for k in range(n+1)] 
    table[0] = 1
    for i in range(0,m): 
        for j in range(S[i],n+1): 
            table[j] += table[j-S[i]]   
    return table[n] 
  
arr = list(map(int,input('Enter the denominations : ').split()))
m = len(arr) 
n = int(input('Enter the cost : '))
x = count(arr, m, n) 
print (x) 