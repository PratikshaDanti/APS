# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:07:38 2020

@author: Pratiksha
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:59:46 2020

@author: Pratiksha
"""

def find(arr,u,v):
    if arr[u]==arr[v]:
        return True
    else:
        return False

def union(arr,a,b,step):
    var=arr[a]
    for i in range(len(arr)):
        if arr[i]==var:
            arr[i]=arr[b]
    print(step,'(',u,v,')',arr)

n=8
    
Dict=dict({
      ((6,7),2), ((2,8),4), ((5,6),4), ((0,1),8), ((1,2),16), ((3,4),18), ((2,5),8),
      ((6,8),12), ((2,3),14), ((7,8),14), ((0,7),16), ((4,5),20), ((1,7),22)
     })

arr=[]
for i in range(n+1):
    arr.append(i)

sorted_dict=sorted(Dict.items(),key=lambda kv:kv[1],reverse=True)
itr=1
cost=0
for i in range(len(sorted_dict)):
    if arr.count(arr[0])==len(arr):
        break
    step=itr
    u=sorted_dict[i][0][0]
    v=sorted_dict[i][0][1]
    x=find(arr,u,v)
    if x == True:
        print(step,'(',u,v,')','Discard')
        itr+=1
    else:
        union(arr,u,v,step)
        cost+=sorted_dict[i][1]
        itr+=1

print('cost : ',cost)