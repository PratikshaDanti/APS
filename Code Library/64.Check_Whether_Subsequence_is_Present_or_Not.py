# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:56:03 2020

@author: Pratiksha
"""

def isPresent(s,s1):
    c=0
    for i in range(len(s)):
        if s1[c]==s[i]:
            c+=1
        if c==len(s1):
            return(True)
    return(False)

s=str(input('Enter the string : '))
s1=str(input('Enter the subsequence : '))
result=isPresent(s,s1)
if (result):
    print('Present')
else:
    print('Not Present')