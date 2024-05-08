#include<stdio.h>
#include<cs50.h>
int main()
{
    long cnumber;
    do
    {
        cnumber = get_long("Number:");
    }
    while(!cnumber);
}
