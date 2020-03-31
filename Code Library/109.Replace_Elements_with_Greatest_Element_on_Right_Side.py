# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:27:53 2020

@author: Pratiksha
"""

def replaceElements(arr):
    for i in range(len(arr)-1):
        arr[i]=(max(arr[i+1:len(arr)]))
    arr[len(arr)-1]=-1
    return(arr)
    
arr=list(map(int,input('Enter array elements : ').split()))
arr=replaceElements(arr)
print('After replacement : ',arr)
