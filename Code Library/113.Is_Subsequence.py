# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:18:01 2020

@author: Pratiksha
"""

def isSubsequence(s, t):
    x=0
    if len(s)==0:
        return True
    elif len(t)>0:
        for i in range(len(t)):
            if s[x]==t[i]:
                x+=1
            if x==len(s):
                return True
            
        return False
    else:
        return False
a,b=map(str,input().split())
x=isSubsequence(a,b)
if x:
    print('Is a Subsequence')
else:
    print('Not a Subsequence')
