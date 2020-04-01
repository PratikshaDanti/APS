# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:43:59 2020

@author: Pratiksha
"""

def countNegatives(grid):
    ctr=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]<0:
                ctr+=1
    return ctr

n=int(input('Enter number of rows : '))
l=[]
for i in range(n):
    a=list(map(int,input('Enter the array elements : ').split()))
    l.append(a)
c=countNegatives(l)
print('Number of negative values are : ',c)
    