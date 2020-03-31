# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:15:44 2020

@author: Pratiksha
"""

d=int(input('Enter the distance after which refill is required : '))
a=list(map(int,input('Enter the gas station locations : ').split()))
total=int(input('Enter the total distance of journey : '))
a.insert(0,0)
a.append(total)
d1=d
ctr=0
for i in range(len(a)-1):
    if(d1-(a[i+1]-a[i]))>=0:
        d1=d1-(a[i+1]-a[i])
    elif a[i+1]-a[i] > d:
        print('not possible')
        break
    else:
        d1=d
        d1=d1-(a[i+1]-a[i])
        ctr+=1

print(ctr)   