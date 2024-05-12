#include<stdio.h>
#include<cs50.h>
#include<string.h>

int main(void)
{
    int no_of_letters=0;
    string text =get_string("Text:");
    for (int i=0,n=strlen(text);i<n;i++)
    {
        if(text[i]!="\ ")
        {
            no_of_letters++;
        }
    }
    printf("%d",no_of_letters);
}
