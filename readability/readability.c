#include<stdio.h>
#include<cs50.h>
#include<string.h>

int no_of_letters(string s);
int no_of_words(string s);
int no_of_sentences(string s)

int main(void)
{
    int letters,words,sentences;
    string text =get_string("Text:");
    letters = no_of_letters(text);
    words = no_of_words(text);
    sentences = no_of_sentences(text);
    float L,S,index;
    L = (letters/words)*100;
    S = (sentences/words)*100;
    index = 0.0588*L - 0.296*S -15.8;

}
int no_of_letters(string s)
{
    int count = 0;
     for (int i=0,n=strlen(text);i<n;i++)
    {
        count++;
    }
}
int no_of_words(string s)
{
    int count =0;
    for (int i=0,n=strlen(text);i<n;i++)
    {
        if (text[i]==' '||text[i]=='.')
            count++;
    }
    return count;
}

int no_of_sentences(string s)
{
    int count=0;
    for (int i=0,n=strlen(text);i<n;i++)
    {
        if (text[i]=='.')
            count++;
    }
    return count;
}
