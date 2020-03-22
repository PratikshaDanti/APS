# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:06:39 2020

@author: Pratiksha
"""

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
val = list(map(int,input('Enter the value array : ').split())) 
wt = list(map(int,input('Enter the weight array : ').split()))
W = int(input('Enter the value : '))
n = len(val) 
print(knapSack(W, wt, val, n)) 
