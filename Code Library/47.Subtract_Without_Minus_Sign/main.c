#include <stdio.h>
#include <stdlib.h>

int subtract(int x,int y)
{
    while(y!=0)
    {
        int borrow=(~x)&y;
        x=x^y;
        y=borrow<<1;
    }
    return x;
}

int main()
{
    int a,b,res;
    printf("Enter two values :");
    scanf("%d%d",&a,&b);
    res=subtract(a,b);
    printf("Difference of 2 numbers is : %d",res);
    return 0;
}
