# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:51:02 2020

@author: Pratiksha
"""
import math
def count_set_bits(n):
    cnt=0
    while(n):
        cnt+=n & 1
        n>>=1
    return cnt

cost=[[3,2,7],[5,1,3],[2,7,2]]
dp=[]
n=3
for i in range(2**n):
    dp.append(math.inf)
dp[0]=0
    
for i in range(2**n):
    x=count_set_bits(i)
    for j in range(n):
        if (i & 1<<j) == 0:
            dp[i | (1<<j)]=min(dp[i | (1<<j)],(dp[i]+cost[x][j]))
            
print(dp)
