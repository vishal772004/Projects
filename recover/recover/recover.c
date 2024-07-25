#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char *argv[])
{
    if(argc!=2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    FILE *card = fopen(argv[1],"r");
    if (card==NULL)
    {
        printf("Could not open file:");
        return 1;
    }
    uint8_t buffer[512];
    
}
