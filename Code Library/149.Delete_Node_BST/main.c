#include <stdio.h>
#include <stdlib.h>

struct node
{
    struct node *left;
    struct node *right;
    int rollno;
}*root;

struct node *insert(struct node *root,int data)
{
    struct node *nw;
    if(root==NULL)
    {
        nw=malloc(sizeof(struct node));
        nw->rollno=data;
        nw->left=nw->right=NULL;
        return nw;
    }
    else
        if(data<root->rollno)
        root->left=insert(root->left,data);
    else
        if(data>root->rollno)
        root->right=insert(root->right,data);
    else
        printf("node exists\n");
    return root;
}

void inorder(struct node *root)
{
    if(root==NULL)
        return;
    inorder(root->left);
    printf("roll no:%d\n",root->rollno);
    inorder(root->right);
}

struct node *delete_node(struct node *root,int rno)
{
    struct node *tmp,*par,*cur;
    par=NULL;
    cur=root;
    while(cur!=NULL &&cur->rollno!=rno)
    {
        par=cur;
        if(cur->rollno<rno)
            cur=cur->left;
        else
            cur=cur->right;
    }
    if(cur==NULL)
      {
        printf("node not found\n");
        return root;
      }
    if(cur->left!=NULL && cur->right!=NULL)
      {
          tmp=par=cur;
          cur=cur->left;
          while(cur!=NULL)
            cur=cur->right;
          tmp->rollno=cur->rollno;
      }
      if(cur->left!=NULL)
      {
          if(cur==root)
            root=root->left;
          else
          {
              if(cur==par->left)
                par->left=cur->left;
              else
                par->right=cur->left;
          }
      }
      else
      if(cur->right!=NULL)
      {
          if(cur==root)
            root=root->right;
          else
          {
              if(cur==par->left)
                par->left=cur->right;
              else
                par->right=cur->right;
          }
      }
      else
      {
          if(cur==root)
            root=NULL;
          else
          {
              if(cur==par->left)
                par->left=NULL;
              else
                par->right=NULL;
          }
      }
      printf("deleted node is:\n");
      printf("%d\n",cur->rollno);
        free(cur);
        return root;
}

int main()
{
    int ch,r;
    do
    {
        printf("1.insert\n2.delete\n3.display\n4.exit\nenter your choice:\n");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:printf("enter roll no to be inserted:\n");
                    scanf("%d",&r);
                    root=insert(root,r);
                    break;

            case 2:printf("enter noll no to be deleted:\n");
                    scanf("%d",&r);
                    root=delete_node(root,r);
                    break;

            case 3:printf("elements are:\n");
                    inorder(root);
                    break;

            case 4:break;
        }
    }while(ch!=4);
    return 0;
}
