#include <stdio.h>
#include <stdlib.h>
#define STACKSIZE 5
int x=300;

struct stack
{
    int s[STACKSIZE];
    int top;
}s1,s2;

void push(struct stack *ps,int data)
{
    ps->s[ps->top] = data;
    //printf("pushed value:%d\n",data);
    (ps->top) = (ps->top)+1;
}

int pop(struct stack *ps)
{
     int data;
     (ps->top) = (ps->top)-1;
     data = ps->s[ps->top];
     printf("popped value:%d\n",data);

     return data;
}

void game(struct stack *s1,struct stack *s2)
{
    int ch;
    int s=0,count=0,val,val1;

    while(s<=x)
    {
        printf("1 or 2\n");
        //fflush(stdin);
        scanf("%d",&ch);
        switch(ch)
        {

            case 1: val = pop(s1);//printf("%d\n",val);
                    s=s+val;printf("%d\n",s);
                    count++;
                    break;

            case 2: val1 = pop(s2);//printf("%d\n",val1);
                   s=s+val1;printf("%d\n",s);
                   count++;
                   break;
        }
    }
    printf("final score:%d %d",count,s);
}

int main()
{
    int ele,i,e;
    s1.top=0;s2.top=0;
    printf("enter 2 stacks:\n");
    for(i=0;i<5;i++)
    {
        scanf("%d",&ele);
        push(&s1,ele);
    }
    for(i=0;i<5;i++)
    {
        scanf("%d",&e);
        push(&s2,e);
    }
    game(&s1,&s2);
    return 0;
}
