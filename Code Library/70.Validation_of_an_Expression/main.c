#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int validate(char infix[])
{
    int i,j,k,p,x=0,y=0,z=1,f=0;
    p=strlen(infix);
    if(infix[0]=='+'||infix[0]=='-'||infix[0]=='*'||infix[0]=='/'||infix[0]=='^')
        return 0;

    if(infix[p-1]=='+'||infix[p-1]=='-'||infix[p-1]=='*'||infix[p-1]=='/'||infix[p-1]=='^')
        return 0;

    for(j=0;infix[j]!='\0';j++)
    {
        if(infix[j]=='(')
            x++;
        if(infix[j]==')')
            y++;
    }
    if(x==y)
        f=1;
    else
        f=0;

    for(k=0;infix[k]!='\0';k++)
    {
        if((infix[k]=='+'||infix[k]=='-'||infix[k]=='*'||infix[k]=='/'||infix[k]=='^')&&(infix[k+1]=='+'||infix[k+1]=='-'||infix[k+1]=='*'||infix[k+1]=='/'||infix[k+1]=='^'))
            return 0;
        if(((infix[k]>='a'&&infix[k]<='z')||(infix[k]>='A'&&infix[k]=='Z')||(infix[k]>='0'&&infix[k]<='9'))&&((infix[k+1]>='a'&&infix[k+1]<='z')||(infix[k+1]>='A'&&infix[k+1]=='Z')||(infix[k+1]>='0'&&infix[k+1]<='9')))
            return 0;
    }

    for(i=1;infix[i]<p-1;i++)
    {

        if(infix[i]=='(')
        {
            if((infix[i-1]!='+' || infix[i-1]!='-' || infix[i-1]!='*' || infix[i-1]!='/' || infix[i-1]!='^'||infix[i-1]!='(')
               ||(infix[i+1]=='+' || infix[i+1]=='-' || infix[i+1]=='*' || infix[i+1]=='/' || infix[i+1]=='^'))
                z=0;
                break;
        }
        else
        if(infix[i]==')')
        {
            if((infix[i+1]!='+' || infix[i+1]!='-' || infix[i+1]!='*' || infix[i+1]!='/' || infix[i+1]!='^' || infix[i+1]==')')
               ||(infix[i-1]=='+' || infix[i-1]=='-' || infix[i-1]=='*' || infix[i-1]=='/' || infix[i-1]=='^'))
                z=0;
                break;
        }
        else
            continue;
    }

    if(f==0&&z==0)
            return 0;
        else
            return 1;
}

void main()
{
    int v;
    char infix[100];
    printf("enter infix expression:\n");
    scanf("%s",infix);
    v=validate(infix);
    if(v==1)
        printf("valid expression\n");
    else
        printf("invalid expression\n");
}
