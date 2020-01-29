#include <stdio.h>
#include <stdlib.h>

int fact(int n)
{
    int i,fac[100];
    fac[0]=1;
    fac[1]=1;
    for(i=2;i<n+1;i++)
    {
        fac[i] = i * fac[i-1];
    }
    return fac[n];
}
int main()
{
    int n,x;
    printf("enter the number :\n");
    scanf("%d",&n);
    x = (fact(2*n))/((fact(n+1))*fact(n));
    printf("Result is : %d\n",x);
    return 0;
}
