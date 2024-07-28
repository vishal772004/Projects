// Implements a dictionary's functionality
#include<stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include<strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
unsigned int size_of = 0;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int hashvalue;
    hashvalue = hash(&word);
    for(node *ptr=table[hashvalue];ptr!=NULL;ptr=ptr->next)
    {
        if(strcasecmp(ptr->word,word)==0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    unsigned int hashvalue;
    FILE *source = fopen(dictionary,"r");
    if (source == NULL)
    {
        return false;
    }
    char *word = NULL;
    while(fscanf(source,"%s",word)!=EOF)
    {
        node *n = malloc(sizeof(node));
        if(n==NULL)
        {
            return false;
        }
        strcpy(n->word,word);
        hashvalue = hash(&word);
        if (table[hashvalue]->next==NULL)
        {
            table[hashvalue]->next = n->next;
            table[hashvalue]->word = n->word;
            n->next = NULL;
        }
        else
        {
            n->next = table[hashvalue]->next;
            table[hashvalue]->word = n->word;
            table[hashvalue]->next = n;
        }
        size_of++;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return size_of;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
