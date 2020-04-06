#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
}*first;

struct node *create_node()
{
    struct node *nw;
    nw=malloc(sizeof(struct node));
    printf("enter data:\n");
    scanf("%d",&nw->data);
    nw->next=NULL;
    return nw;
}

struct node *create_list()
{
    struct node *nw,*tmp;
    tmp=first;
    nw=create_node();
    if(first==NULL)
    {
        first=nw;
        return first;
    }
    else if(first->next==NULL)
    {
        first->next=nw;
    }
    else
    {
        while(tmp->next!=NULL)
            tmp=tmp->next;
        tmp->next=nw;
    }
    return first;
}

struct node *reverse_list()
{
    struct node *t1,*t2,*t3;
    t1=NULL;
    t2=first;
    t3=t2->next;
    do
    {
    t2->next=t1;
    t1=t2;
    t2=t3;
    if(t3!=NULL)
        t3=t3->next;
    }while(t2!=NULL);
    return t1;
}

void display()
{
    struct node *tmp=first;
    if(tmp==NULL)
        printf("no nodes\n");
    else
    {
        while(tmp!=NULL)
        {
            printf("%d\t",tmp->data);
            tmp=tmp->next;
        }
    }
}

int main()
{
    int ch;
    first=NULL;
    do
    {
        printf("1.create list\n2.reverse list\n3.display\n4.exit\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:first=create_list();
                    break;

            case 2:first=reverse_list();
                    break;

            case 3:display();
                    printf("\n");
                    break;

            case 4:break;
        }
    }while(ch!=4);
    return 0;
}
