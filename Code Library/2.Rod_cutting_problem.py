n=int(input('enter the length: '))
li=[]
x=0
li.append(0)
li.append(0)
for i in range(2,n+1):
    for j in range(1,i//2+1):
        x=max(li[j],j*(i-j),j*li[i-j])
    li.append(x)
    
print(li)
