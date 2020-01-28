#include <stdio.h>
#include <stdlib.h>

int max_val(int a,int b,int c)
{
    if(a>b && a>c)
    {
        return a;
    }
    if(b>a && b>c)
    {
        return b;
    }
    return c;
}

void rod_cutting(int n)
{
    int i,j,a[100];
    a[0]=0;
    a[1]=0;
    for(i=2;i<n+1;i++)
    {
        a[i]=0;
        for(j=1;j<i/2+1;j++)
        {
            a[i] = max_val(a[i],(j*(i-j)),(j*a[i-j]));
        }
    }
    for (i=0;i<n+1;i++)
    {
        printf("%d ",a[i]);
    }
}
int main()
{
    int n;
    printf("enter the length:\n");
    scanf("%d",&n);
    printf("result is:\n");
    rod_cutting(n);
    return 0;
}
