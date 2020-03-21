#include <stdio.h>
#include <stdlib.h>

int add(int x,int y)
{
    while(y!=0)
    {
        int carry=x&y;
        x=x^y;
        y=carry<<1;
    }
    return x;
}

int main()
{
    int a,b,res;
    printf("Enter two values :");
    scanf("%d%d",&a,&b);
    res=add(a,b);
    printf("Sum of 2 numbers is : %d",res);
    return 0;
}
