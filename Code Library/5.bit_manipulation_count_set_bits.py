# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:41:37 2020

@author: Pratiksha
"""

n=int(input('enter the number : '))
ctr=0
while(n!=0):
    n = n & (n-1)
    ctr=ctr+1
    
print(ctr)