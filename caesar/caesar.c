#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>

int main(int argc,string argv[])
{
    if(argc==2)
    {
        if (isdigit(argv))
        {
            string plaintext = get_string("plaintext:");
            print(cipher(plaintext,argv));
            return 0;
        }
        else
        {
            printf("Usage: ./caesar key");
            return 1;
        }
    }
    else
    {
        printf("Usage: ./caesar key");
        return 1;
    }
}
string cipher(string s,string k)
{
    for (int i=0,n=strlen(s);i<n;i++)
    {
        
    }
}
