# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:09:03 2020

@author: Pratiksha
"""

n,k=map(int,input('Enter n and k values : ').split())
import numpy as np
bc=[]
li=[]
for j in range(k+1):
    li.append(0)
for i in range(n+1):
    bc.append(li)
bc=np.array(bc)            
    
for i in range(0,n+1):
    for j in range(0,min(i,k)+1):
        if j==0 or j==i:
            bc[i][j]=1
        else:
            bc[i][j]=bc[i-1][j-1]+bc[i-1][j]
print(bc[n][k])