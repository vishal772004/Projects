#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>

string cipher(string s,string k);

int main(int argc,string argv[])
{
    if(argc==2)
    {
            string plaintext = get_string("plaintext:");
            printf(cipher(plaintext,argv[]));
            return 0;
    }
    else
    {
        printf("Usage: ./caesar key");
        return 1;
    }
}
string cipher(string s,string k)
{
    string ciphertext;
    int key = atoi(k);
    for (int i=0,n=strlen(s);i<n;i++)
    {
            ciphertext = s[i]+key;
    }
    return ciphertext;
}
