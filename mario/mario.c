#include<stdio.h>
#include<cs50.h>
int main()
{
    int height;
    do
    {
         height = get_int("Height:");
    }while(height<=0);

    for (int i=0;i<height;i++)
    {
        for (int j=0;j<height;j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
