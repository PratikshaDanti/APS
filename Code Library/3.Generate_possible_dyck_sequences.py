# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:16:15 2020

@author: Pratiksha
"""

n=int(input())
y=[]
def toString(List): 
    return ''.join(List) 
def permute(a, l, r): 
    if l==r:
        if toString(a) not in y:
            y.append(toString(a))
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]

string=""

for i in range(n):
    string=string+'x'
    string=string+'y'

n = len(string) 
a = list(string) 
permute(a, 0, n-1)     
y1=[]
for k in y:
    given=k
    ctr=0
    f=0
    for i in range(len(given)):
        if given[i]=='x':
            ctr=ctr+1
        else:
            ctr=ctr-1
            if ctr<0:
                f=1
                break
    if f!=1:
        y1.append(given)
        
print(y1)
            
        
        
        
        
