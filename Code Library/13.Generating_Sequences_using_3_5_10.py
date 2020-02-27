# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:11:25 2020

@author: Pratiksha
"""
total=15
n=total+1
li=[]
li1=[]
li2=[]
for i in range(n):
    li.append(0)
li[0]=1
for i in range(3,n):
    li[i]=li[i-3]+li[i]

for i in range(5,n):
    li[i]=li[i-5]+li[i]
    
for i in range(10,n):
    li[i]=li[i-10]+li[i]
print(li)
req=int(input('enter the number : '))
i=0
j=req
while(i<req/2):
    if i+j==req:
        if li[i]==0 or li[j]==0:
            i=i+1
            j=j-1
        else:
            li1.append([i,j])
            i=i+1
            j=j-1
    else:
        i=i+1
        j=j-1

#print(li1)
li2=[]           
for i in range(len(li1)):
    l=[]
    x=(li1[i][0])
    if (x%3==0 or x%5==0 or x%10==0):
        while(x!=0):
            if x%10==0:
                l.append(10)
                x=x-10
            elif x%5==0:
                l.append(5)
                x=x-5
            elif x%3==0:
                l.append(3)
                x=x-3
    x=(li1[i][1])
    if (x%3==0 or x%5==0 or x%10==0):
        while(x!=0):
            if x%10==0:
                l.append(10)
                x=x-10
            elif x%5==0:
                l.append(5)
                x=x-5
            elif x%3==0:
                l.append(3)
                x=x-3
        
    if l not in li2:
        li2.append(l)

    l=[]
    x=(li1[i][0])
    if (x%3==0 or x%5==0 or x%10==0):
        while(x!=0):
            if x%5==0:
                l.append(5)
                x=x-5
            elif x%10==0:
                l.append(10)
                x=x-10
            elif x%3==0:
                l.append(3)
                x=x-3
            
    x=(li1[i][1])
    if (x%3==0 or x%5==0 or x%10==0):
        while(x!=0):
            if x%5==0:
                l.append(5)
                x=x-5
            elif x%10==0:
                l.append(10)
                x=x-10
            elif x%3==0:
                l.append(3)
                x=x-3
        
    if l not in li2:
        li2.append(l) 
li3=[]        
for i in range(len(li2)):
    s=0
    if len(li2)>0:
        p=len(li2[i])
        for j in range(p):
            s=s+li2[i][j]
        if s==req:
            li3.append(li2[i])
print('possible sequences are :\n',li3)
