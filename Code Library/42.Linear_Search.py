# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:47:10 2020

@author: Pratiksha
"""

def linearSearch(a,ele):
    for i in a:
        if i==ele:
            return True
    return False

a=list(map(int,input('Enter the array elements : ').split()))
element=int(input('Enter the element to be searched : '))
x=linearSearch(a,element)
if x==False:
    print('Element not found')
else:
    print('Element found')