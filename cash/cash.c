#include<stdio.h>
#include<cs50.h>
int main()
{
    int cash;
    do
    {
        cash = get_int("Change owed?");
    }
    while(cash<0);
    
}
