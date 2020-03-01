import numpy as np
ss=list(map(int,input('Enter the items : ').split()))
sm=int(input('Enter the expected sum : '))
li=[]
a=[]
for i in range(sm+1):
    li.append(False)
for i in range(len(ss)+1):
    a.append(li)
a=np.array(a)
for i in range(len(ss)+1):
    a[i][0]=True
    
for i in range(1,len(ss)+1):
    for j in range(1,sm+1):
        if a[i-1][j] == True:
            a[i][j] = True
        else:
            if ss[i-1]>j:
                a[i][j] = False
            else:
                a[i][j] = a[i-1][j-ss[i-1]]
print(a)
print(a[len(ss)][sm])