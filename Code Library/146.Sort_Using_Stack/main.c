#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int top;
    int data[10];
}s1,s2;

void push(int s,struct stack *stk)
{
    (stk->top) = (stk->top)+1;
    stk->data[stk->top]=s;
}

int pop(struct stack *stk)
{
    int s;
    s=stk->data[stk->top];
    (stk->top)=(stk->top)-1;
    return s;
}

int main()
{
    int i,a[10],e;
    s1.top=s2.top=-1;
    printf("enter 10 elements:\n");
    for(i=0;i<10;i++)
        scanf("%d",&a[i]);

        for(i=0;i<10;i++)
    {
        if(s1.top==-1)
            {
                push(a[i],&s1);
            }
            else
            {
                while(s1.top>=0)
                {
                    if(a[i]<s1.data[s1.top])
                    {
                        e=pop(&s1);
                        push(e,&s2);
                    if(s1.top==-1)
                        {
                            push(a[i],&s1);
                            break;
                        }
                    }
                    else
                    {
                        push(a[i],&s1);
                        break;
                    }
                }
                    while(s2.top>=0)
                    {
                        e=pop(&s2);
                        push(e,&s1);
                    }
                }
            }
for(i=0;i<=s1.top;i++)
    printf("%d\t",s1.data[i]);

    return 0;
}
