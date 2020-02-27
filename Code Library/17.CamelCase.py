# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:51:27 2020

@author: Pratiksha
"""

def camelcase(s):
    ctr=0
    for i in range(len(s)):
        if s[i].isupper()==True:
            ctr+=1
    return (ctr+1)

if __name__ == '__main__':
    s=str(input('Enter the string : '))
    x=camelcase(s)
    print('Number of words : ',x)