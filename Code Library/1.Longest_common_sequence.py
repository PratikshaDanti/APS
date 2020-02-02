# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:32:37 2020

@author: Pratiksha
"""

s1 = str(input('Enter string 1 '))
s2 = str(input('Enter string 2 '))
li1=[]
li=[]

for i in range(len(s2)+1):
    li.append(0)
for i in range(len(s1)+1):
    li1.append(li)
    
p=0
k=0
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[k]==s2[j-1]:
            li1[i][j]=(li1[i-1][j-1]+1)
        else:
            li1[i][j]=(max(li1[i-1][j],li1[i][j-1]))
    k=k+1
        
print('Length of longest common subsequence ',li1[len(s1)][len(s2)])
