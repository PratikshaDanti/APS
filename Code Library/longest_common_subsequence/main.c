#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max_val(int a,int b)
{
    if(a>b)
    return a;
    return b;
}

void lcc(int n1,char s1[],int n2,char s2[])
{
    int i,j,k;
    int m[100][100];
    j=0;
    for(i=0;i<n2+1;i++)
    {
        m[j][i]=0;
    }
    j=0;
    for(i=0;i<n1+1;i++)
    {
        m[i][j]=0;
    }
    k=0;
    for(i=1;i<n1+1;i++)
    {
        for(j=1;j<n2+1;j++)
        {
            if(s1[k]==s2[j-1])
            {
                m[i][j] = m[i-1][j-1]+1;
            }
            else
            {
                m[i][j] = max_val((m[i-1][j]),(m[i][j-1]));
            }
        }
        k++;
    }
    printf("\nLongest common subsequence is : %d\n\n",m[n1][n2]);
    for(i=0;i<n1+1;i++)
    {
        for(j=0;j<n2+1;j++)
        {
            printf("%d ",m[i][j]);
        }
        printf("\n");
    }
}
int main()
{
    int n1,n2;
    char s1[100],s2[100];
    printf("enter the string 1 : ");
    scanf("%s",s1);
    printf("enter the string 2 : ");
    scanf("%s",s2);
    n1=strlen(s1);
    n2=strlen(s2);
    lcc(n1,s1,n2,s2);
    return 0;
}
