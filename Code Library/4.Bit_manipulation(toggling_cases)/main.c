#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("enter lower case character and upper case character for conversion :\n");
    char c1,c2;
    scanf("%c %c",&c1,&c2);
    printf("Before conversion : \n%c\n%c\n",c1,c2);
    c1 = c1 & ~32;
    c2 = c2 | 32;
    printf("After conversion : \n%c\n%c\n",c1,c2);
    return 0;
}
