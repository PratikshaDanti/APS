# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:48:20 2020

@author: Pratiksha
"""

def selfDividingNumbers(left,right):
    l1=[]
    for i in range(left,right+1):
        s=str(i)
        if '0' in s:
            continue
        l=[]
        for ele in s:
            l.append(int(ele))
        f=0
        for ele in l:
            if i % ele == 0:
                f=1
            else:
                f=0
                break
        if f==1:
            l1.append(i)
    return(l1)
    
a,b=map(int,input('Enter range : ').split())
arr=selfDividingNumbers(a,b)
print(arr)