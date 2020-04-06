#include <stdio.h>
#include <stdlib.h>
#define QSIZE 5

typedef struct
{
    int processId;
    char processName[20];
    int size;
}Process;

typedef struct
{
    Process q[QSIZE];
    int front,rear;
}Queue;

int isFull(Queue *cq)
{
    if(((cq->rear+1)%QSIZE)==(cq->front))
        return 1;
    else
        return 0;
}

int isEmpty(Queue *cq)
{
    if(cq->front==cq->rear)
        return 1;
    else
        return 0;
}

void readProcess(Process *p)
{
    printf("enter process details:\n");
    scanf("%d%s%d",&p->processId,p->processName,&p->size);
}

void displayProcess(Process p)
{
    printf("process details:\n");
    printf("process id:%d\nprocess name:%s\nprocess size:%d\n",p.processId,p.processName,p.size);
}

void displayAllProcess(Queue cq)
{
    int i;
    printf("process in queue are:\n");
    i=cq.front;
    while(i!=cq.rear)
    {
        i=(i+1)%QSIZE;
        displayProcess(cq.q[i]);
    }
}

void insertProcess(Queue *cq,Process p)
{
    if(!isFull(&cq))
    {
    cq->rear=((cq->rear+1)%QSIZE);
    cq->q[cq->rear]=p;
    }
    else
        printf("queue full\n");
}

Process deleteProcess(Queue *cq)
{
    Process p;
    if(!isEmpty(&cq))
    {
        cq->front=(cq->front+1)%QSIZE;
        p=cq->q[cq->front];
        return p;
    }
    else
        printf("queue empty\n");
}
void main()
{
    Queue cq;
    Process p;
    int ch;
    cq.front=cq.rear=QSIZE-1;
    do
    {
        printf("1->insert process\n2->delete process\n3->display processes\n4->exit\n");
        printf("enter choice:\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1: if(!isFull(&cq))
                    readProcess(&p);
                    insertProcess(&cq,p);
                    break;

            case 2: printf("deleted process is:\n");
                    p=deleteProcess(&cq);
                    displayProcess(p);
                    break;

            case 3: if(isEmpty(&cq))
                    printf("queue empty\n");
                    else
                    displayAllProcess(cq);
                    break;

            case 4: break;

        }
    }while(ch!=4);
}
