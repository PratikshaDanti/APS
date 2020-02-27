# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:41:01 2020

@author: Pratiksha
"""

def pangrams(s):
    s=s.lower()
    s=s.replace(' ',"")
    li=[]
    for i in range(len(s)):
        if s[i] not in li:
            li.append(s[i])
    if len(li)==26:
        return('pangram')
    return('not pangram')
    
if __name__ == '__main__':
    s=str(input('Enter the string : '))
    x=pangrams(s)
    print(x)