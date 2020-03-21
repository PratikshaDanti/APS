#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define STACKSIZE 100

typedef struct
{
    double S[STACKSIZE];
    int top;
}Stack;

void push(Stack *ps,double data)
{
    ps->top=ps->top+1;
    ps->S[ps->top]=data;
}

double pop(Stack *ps)
{
    double data=ps->S[ps->top];
    ps->top=ps->top-1;
    return data;
}

double evalPrefix(char pref[])
{
    double op1,op2,res;
    char inp;
    Stack stack;
    int i;
    stack.top=-1;
    strrev(pref);
    for(i=0;(inp=pref[i])!='\0';i++)
    {
        if(isalpha(inp))
        {
            printf("enter value of variable %c\n",inp);
            scanf("%lf",&res);
            push(&stack,res);
        }
        else if(isdigit(inp))
        {
            res=inp-'0';
            push(&stack,res);
        }
        else
        {
            op1=pop(&stack);
            op2=pop(&stack);
            switch(inp)
            {
                case '+' : res=op1+op2;
                           break;

                case '-' : res=op1-op2;
                           break;

                case '*' : res=op1*op2;
                           break;

                case '/' : res=op1/op2;
                           break;
            }
            push(&stack,res);
        }
    }
    return(pop(&stack));
}

void main()
{
    char prefix[100];
    double res;
    printf("enter prefix expression:\n");
    scanf("%s",prefix);
    res=evalPrefix(prefix);
    printf("result:%lf",res);
}

