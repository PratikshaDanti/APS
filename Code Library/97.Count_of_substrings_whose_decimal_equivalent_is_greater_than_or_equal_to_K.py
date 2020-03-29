# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:40:08 2020

@author: Pratiksha

"""

from itertools import combinations
test_str=str(input('Enter the string : '))
k=int(input('Enter value of k : '))
l=[]
li=[]
res = [test_str[x:y] for x, y in combinations( 
            range(len(test_str) + 1), r = 2)] 

print(res)
for i in res:
    x=int(i,2)
    print(x)
    if x>=k :
        li.append(x)
print(li)