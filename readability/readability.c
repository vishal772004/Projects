#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<math.h>

int no_of_letters(string s);
int no_of_words(string s);
int no_of_sentences(string s);

int main(void)
{
    int letters,words,sentences;
    string text =get_string("Text:");
    letters = no_of_letters(text);
    words = no_of_words(text);
    sentences = no_of_sentences(text);
    float L,S,index;
    L = (letters/(float)words)*100;
    S = (sentences/(float)words)*100;
    index = 0.0588*L - 0.296*S -15.8;
    if (index>=16)
    {
        printf("Grade 16+");
    }
    else if(index<=1)
    {
        printf("Before Grade 1");
    }
    else
    {
        printf("Grade %i",(int)round(index));
    }

    printf("\n");
}
int no_of_letters(string s)
{
    int count = 0;
     for (int i=0,n=strlen(s);i<n;i++)
    {
        if (s[i]==' '||s[i]=='.'|| s[i]=='!'||s[i]=='?'||s[i]==',')
            continue;
        count++;
    }
    return count;
}
int no_of_words(string s)
{
    int count =0;
    for (int i=0,n=strlen(s);i<n;i++)
    {
        if (s[i]==' ')
            count++;
    }
    return count+1;
}

int no_of_sentences(string s)
{
    int count=0;
    for (int i=0,n=strlen(s);i<n;i++)
    {
        if (s[i]=='.' || s[i]=='!' || s[i]=='?')
            count++;
    }
    return count;
}
