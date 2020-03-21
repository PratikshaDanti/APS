#include <stdio.h>
#include <stdlib.h>

int c=0;
int flag=0;
int main()
{
    int allocation[10][10],need[10][10],maximum[10][10],available[10][10];
    int m,n,i,j,nx[10],av[10],seq[10];
    int s;
    printf("enter no. of processes:\n");
    scanf("%d",&m);
    printf("enter no. of resources:\n");
    scanf("%d",&n);
    printf("enter max resources:\n");
    for(i=0;i<n;i++)
        scanf("%d",&nx[i]);
    printf("enter allocation values\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&allocation[i][j]);
        }
    }
    printf("enter maximum values\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&maximum[i][j]);
        }
    }
    printf("need values are:\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            need[i][j]=maximum[i][j]-allocation[i][j];
            printf("%d ",need[i][j]);
        }
        printf("\n");
    }
    for(i=0;i<n;i++)
    {
        s=0;
        for(j=0;j<m;j++)
        {
            s=s+allocation[j][i];
        }
        av[i]=nx[i]-s;
    }
    printf("initial available values are:\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",av[i]);
    }
    printf("\n");
    printf("available values are:\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
            available[i][j]=-1;
    }

    for(i=0;i<m;i++)
    {
        for(j=0;j<m;j++)
        {
                if(av[0]>=need[j][0] && av[1]>=need[j][1]&& av[2]>=need[j][2] && available[j][0]==-1)
                {
                    available[j][0]=av[0]+allocation[j][0];
                    available[j][1]=av[1]+allocation[j][1];
                    available[j][2]=av[2]+allocation[j][2];
                    av[0]=available[j][0];
                    av[1]=available[j][1];
                    av[2]=available[j][2];
                    seq[c]=j;
                    c++;
                }
            }
    }
    for(i=0;i<m;i++)
    {
            if(available[0][i]==-1)
                {
                    flag=-1;
                    break;
                }
    }
        if(flag==-1)
        {
            printf("it is a deadlock");
            exit(0);
        }
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",available[i][j]);
        }
        printf("\n");
    }
    printf("it is in safe state\n");
    printf("sequence of execution is:\n");
    for(i=0;i<m;i++)
    {
        printf("process P%d\n",seq[i]);
    }
    return 0;
}
