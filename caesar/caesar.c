#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>

void cipher(string s,int k);

int main(int argc,string argv[])
{
    int count =0;
    for (int i=0,n=strlen(argv[1]);i<n;i++)
    {
        if(!isdigit(argv[1][i]))
            count++;
    }
    if(argc==2 && count==0)
    {
            string plaintext = get_string("plaintext:");
            int k = atoi(argv[1]);
            cipher(plaintext,k);
            printf("\n");
            return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
void cipher(string s,int k)
{
    int temp=0;
    char ciphertext[]="";
    printf("ciphertext:");
    for (int i=0,n=strlen(s);i<n;i++)
    {
        if(!isalpha(s[i]))
        {
            printf("%c",s[i]);
            continue;
        }

        temp=s[i]+k;
            if(islower(s[i]))
            {
                while(temp>122)
                {
                    temp = (temp - 122) + 97;

                }
                printf("%d\n",temp);
                temp--;
            }
            else if(isupper(s[i]) && temp>90)
            {
                while(temp>90)
                    temp = (temp - 90) + 65;
                temp--;
            }

        printf("%c\n",temp);
    }

}
