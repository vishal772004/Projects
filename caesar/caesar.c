#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>

void cipher(string s,int k);

int main(int argc,string argv[])
{
    if(argc==2)
    {
            string plaintext = get_string("plaintext:");
            int k = atoi(argv[1]);
            cipher(plaintext,k);
            printf("\n");
            return 0;
    }
    else
    {
        printf("Usage: ./caesar key");
        return 1;
    }
}
void cipher(string s,int k)
{
    char ciphertext[]="";
    for (int i=0,n=strlen(s);i<n;i++)
    {
        if(k>=26)
        {
            if(islower(s))
            {
                
            }
        }
        printf("%c",s[i]+k);
    }

}
