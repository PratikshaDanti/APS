# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 07:49:24 2020

@author: Pratiksha
"""

def printAllKLength(set,k):
    n=len(set)
    printAllKlengthRec(set,'',n,k)
    
def printAllKlengthRec(set,prefix,n,k):
    if k==0:
        print(prefix)
        return
    for i in range(n):
        newprefix=prefix+set[i]+'\t'
        printAllKlengthRec(set,newprefix,n,k-1)

set=['True','False']
n=int(input('Enter the size : '))
printAllKLength(set,n)