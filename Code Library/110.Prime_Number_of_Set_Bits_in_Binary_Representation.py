# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:31:33 2020

@author: Pratiksha
"""

def countPrimeSetBits(L,R):
    l=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    count=0
    for i in range(L,R+1):
        bval=bin(i)
        bval=(bval[2:])
        cnt=bval.count('1')
        if cnt in l:
            count=count+1
    return(count)
    
a,b=map(int,input('Enter the range : ').split())
x=countPrimeSetBits(a,b)
print(x)
