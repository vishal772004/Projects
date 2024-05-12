#include<stdio.h>
#include<cs50.h>
#include<string.h>

int main(void)
{
    int no_of_letters=0,no_of_words=0,no_of_sentences=0;
    string text =get_string("Text:");
    for (int i=0,n=strlen(text);i<n;i++)
    {
        if (text[i]==' '||text[i]=='.')
            no_of_words++;
        if (text[i]=='.')
            no_of_sentences++;
        no_of_letters++;
    }
    printf("%d\n",no_of_letters);
    printf("%d\n",no_of_words);
    printf("%d\n",no_of_sentences);
}
