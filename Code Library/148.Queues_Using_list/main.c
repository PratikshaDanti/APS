#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int rollno;
    char name[20];
}Student;

void readStudent(Student *s)
{
    printf("enter details:\n");
    scanf("%d%s",&s->rollno,s->name);
}

void displayStudent(Student s)
{
    printf("%d\t%s\n",s.rollno,s.name);
}

 typedef struct N
{
    Student data;
    struct N *next;
}Node;

 Node *getNode()
{
    return(malloc(sizeof(Node)));
}

void freeNode(Node *p)
{
    free(p);
}

void displayList(Node *cur)
{   printf("roll.no\tname\n");
    for(;cur!=NULL;cur=cur->next)
    displayStudent(cur->data);
}

Node *insertRear(Node *first)
{
    Node *nw,*prev;
    nw=getNode();
    readStudent(&nw->data);
    nw->next=NULL;
    if(first==NULL)
        first=nw;
    else
    {
        for(prev=first;prev->next!=NULL;prev=prev->next);
        prev->next=nw;
    }
    return first;
}

Node *deleteFront(Node *first)
{
    Node *cur;
    if(first==NULL)
    printf("list empty\n");
    else
    {
        cur=first;
        first=first->next;
        printf("deleted node is:\n");
        displayStudent(cur->data);
        freeNode(cur);
    }
    return(first);
}

Node *createList()
{
    Node *nw,*first,*prev;
    int ch;
    nw=first=prev=NULL;
    do
    {
        prev=nw;
        nw=getNode();
        readStudent(&nw->data);
        if(first==NULL)
            first=nw;
        else
            prev->next = nw;
        printf("1->continue next record\n0-exit\n");
        scanf("%d",&ch);
    }while(ch==1);
    nw->next=NULL;
    return(first);
}

int main()
{
    Node *first =NULL;
    int ch;
    first=createList();
    do
    {
        printf("1->insert \n2->delete\n3->display list\n4->exit\n");
        printf("enter your choice:\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:first=insertRear(first);
                    break;

            case 2: first=deleteFront(first);
                    break;

            case 3: displayList(first);
                    break;

            case 4: break;
        }
    }while(ch!=4);
    return 0;
}
