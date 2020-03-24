#include <stdio.h>
#include <stdlib.h>

int symmetric(int a[10][10],int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(a[i][j]!=a[j][i])
                return 0;
        }
                return 1;
    }
}

int main()
{
    int n,p,i,j,a[10][10];
    printf("enter order of matrix:\n");
    scanf("%d",&n);
    printf("enter elements:\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
            scanf("%d",&a[i][j]);
    }
    p=symmetric(a,n);
    if(p==1)
        printf("symmetric\n");
    else
        printf("not symmetric\n");
    return 0;
}
