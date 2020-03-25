# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:33:00 2020

@author: Pratiksha
"""

def findDuplicate(arr):
    liDuplicate=[]
    dict={}
    for i in arr:
        if i not in dict:
            dict[i]=1
        else:
            liDuplicate.append(i)
    return liDuplicate
     
arr=list(map(int,input('Enter the array elements : ').split()))
print(findDuplicate(arr))
