#include <stdio.h>
#include <stdlib.h>

void compute_357(int arr[],int n)
{
    int i;
    arr[0]=1;
    for(i=3;i<16;i++)
    {
        arr[i]=arr[i]+arr[i-3];
    }

    for(i=5;i<16;i++)
    {
        arr[i]=arr[i]+arr[i-5];
    }

    for(i=10;i<16;i++)
    {
        arr[i]=arr[i]+arr[i-10];
    }
    for(i=0;i<16;i++)
    {
        printf("%d ",arr[i]);
    }
}
int main()
{
    //number of ways to reach 15 using 3,5,10;
    int arr[]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    compute_357(arr,16);
    return 0;
}
