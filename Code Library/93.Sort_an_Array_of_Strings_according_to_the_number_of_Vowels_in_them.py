# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:03:52 2020

@author: Pratiksha
"""

li=list(map(str,input('Enter the array of words : ').split()))
l=[]
l1=[]
for i in (li):
    x=i.count('a')+i.count('e')+i.count('i')+i.count('o')+i.count('u')
    l.append(x)
    l1.append(x)
l1=set(l1)
l1=list(l1)
l1.sort()
res=[]
for i in l1:
    for j in range(len(l)):
        if l[j]==i:
            res.append(li[j])
print(res)
