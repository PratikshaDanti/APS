# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:02:16 2020

@author: Pratiksha
"""

import numpy as np
ss=list(map(int,input('Enter the items : ').split()))
sm=int(input('Enter the expected sum : '))
li=[]
a=[]
for i in range(sm+1):
    li.append(0)
for i in range(len(ss)+1):
    a.append(li)
a=np.array(a)
for i in range(len(ss)+1):
    a[i][0]=1
    
for i in range(1,len(ss)+1):
    for j in range(1,sm+1):
        if a[i-1][j] == 1:
            a[i][j] = 1
        else:
            if ss[i-1]>j:
                a[i][j] = 0
            else:
                a[i][j] = a[i-1][j-ss[i-1]]
print(a)
print(a[len(ss)][sm])