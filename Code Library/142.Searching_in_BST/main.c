#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left,*right;
};
struct node *createbst(struct node *root,int item)
{
    if(root==NULL)
    {
        root=(struct node *)malloc(sizeof(struct node));
        root->left=root->right=NULL;
        root->data=item;
        return root;
    }
    else
    {
        if(item<root->data)
            root->left=createbst(root->left,item);
        if(item>root->data)
            root->right=createbst(root->right,item);
    }
    return (root);  //returns actual root
}

struct node *search(struct node *root,int key)
{
    if(root==NULL)
    {
       printf("data not found\n");
       return;
    }

    else
    {
        if(root->data==key){
           printf("found\n");
           return;
        }
        if(key<root->data)
            root->left=search(root->left,key);
        if(key>root->data)
            root->right=search(root->right,key);
    }
    return (root);
}


void inorder(struct node *root)  //to display
{
    if(root!=NULL)
    {
        inorder(root->left);
        printf("%d\n",root->data);
        inorder(root->right);
    }
}

int maxdepth(struct node *root)
{
    int left,right;
    if(root==NULL)
        return 0;
    else
    {
        left=maxdepth(root->left);
        right=maxdepth(root->right);
    }
    if(left>right)
        return (left+1);
    else
        return (right+1);
}

int main()
{
  int c,key,item;

  struct node *root=NULL;
  for(;;)
  {

  printf("1 insert \n2 search\n enter choice:\n");
  scanf("%d",&c);
  switch(c)
  {
      case 1:
         printf("\n enter data for node");
         scanf("%d",&item);
         root=createbst(root,item);
      break;

      case 2:if(root==NULL)
        printf("empty\n");
        else
        {
          printf("enter key to be searched:\n");
      scanf("%d",&key);
        search(root,key);
        }
        break;
        case 3:inorder(root);
        break;

        case 4: key=maxdepth(root);
                printf("depth =%d",key);
                break;

        case 5: break;
  }
}
}
