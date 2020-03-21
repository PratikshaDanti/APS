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

double evalPostfix(char postf[])
{
    double op1,op2,res;
    char inp;
    Stack stack;
    int i;
    stack.top=-1;
    for(i=0;(inp=postf[i])!='\0';i++)
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
            op2=pop(&stack);
            op1=pop(&stack);
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
    char postfix[100];
    double res;
    printf("enter postfix expression:\n");
    scanf("%s",postfix);
    res=evalPostfix(postfix);
    printf("result:%lf",res);
}
