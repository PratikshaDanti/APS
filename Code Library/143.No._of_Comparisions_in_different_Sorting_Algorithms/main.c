#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void read_arr(int a[],int b[],int c[],int n)
{
    int i,x;
    for(i=0;i<n;i++)
    {
        scanf("%d",&x);
        a[i]=x;
        b[i]=x;
        c[i]=x;
    }
}

void bubble_sort(int a[],int n)
{
    int i,j,x,tmp,flag=0;
    for(i=0;i<n-1;i++)
    {
        x=0;
        for(j=0;j<n-i-1;j++)
       {
           flag++;
           if(a[j]>a[j+1])
        {
            x=1;
            tmp=a[j];
            a[j]=a[j+1];
            a[j+1]=tmp;
        }
       }
       if(x==0)
        break;
    }
    for(i=0;i<n;i++)
        printf("%d\t",a[i]);
    printf("no. of comparisions:%d\n",flag);
}

void selection_sort(int b[],int n)
{
    int i,j,minim,tmp,flag=0;
    for(i=0;i<n-1;i++)
    {
        minim=i;
        for(j=i+1;j<n;j++)
        {
            flag++;
            if(b[j]<b[minim])
                minim=j;
        }
        tmp=b[i];
        b[i]=b[minim];
        b[minim]=tmp;
    }
    for(i=0;i<n;i++)
        printf("%d\t",b[i]);
    printf("no. of comparisions:%d\n",flag);
}

void insertion_sort(int c[],int n)
{
    int i,j,key,flag=0;
    for(i=1;i<n;i++)
    {
        flag++;
        key=c[i];
        j=i-1;
        while(j>=0 && c[j]>key)
        {
        flag++;
            c[j+1]=c[j];
            j--;
        }
        c[j+1]=key;
    }
    for(i=0;i<n;i++)
        printf("%d\t",c[i]);
    printf("no. of comparisions:%d\n",flag);
}

int main()
{
    int ch,a[50000],b[50000],c[50000],n;
    printf("enter no. of values:\n");
    scanf("%d",&n);
    read_arr(a,b,c,n);
    do
    {
        printf("1.bubble sort\n2.selection sort\n3.insertion sort\n4.exit\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1: bubble_sort(a,n);
                    printf("\n");
                    break;

            case 2: selection_sort(b,n);
                    printf("\n");
                    break;

            case 3: insertion_sort(c,n);
                    printf("\n");
                    break;

            case 4:break;
        }
    }while(ch!=4);
    return 0;
}
