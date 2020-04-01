# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:31:17 2020

@author: Pratiksha
"""

def prefixesDivBy5(A):
    x=str(A[0])
    li=[]
    A[0]=int(x)
    x=int(x,2)
    if x%5==0:
        li.append(True)
    else:
        li.append(False)
    for i in range(1,len(A)):
        x=''
        x=str(A[i-1])+str(A[i])
        A[i]=int(x)
        x=int(x,2)
        if x%5==0:
            li.append(True)
        else:
            li.append(False)
    return li
a=list(map(int,input('Enter the array elements : ').split()))
l=prefixesDivBy5(a)
print(l)