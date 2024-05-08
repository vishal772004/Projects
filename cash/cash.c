#include<stdio.h>
#include<cs50.h>
int main()
{
    int cash,coins=0;
    do
    {
        cash = get_int("Change owed?");
    }
    while(cash<0);
    while(cash!=0)
    {
       if(cash>25)
       {
        cash-=25;
        coins++;
       }
       else if(cash>10)
       {
        cash-=10;
        coins++;
       }
       else if(cash>5)
       {
        cash-=5;
        coins++;
       }
       else
       {
        cash-=1;
        coins++;
       }
    }
    printf(coins);
}
