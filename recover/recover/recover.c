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
    int n=0;
    while (fread(&buffer, 1, 512, card) == 512)
    {
            if(buffer[0]==0xff && buffer[1]==0xd8 && buffer[2]==0xff && (buffer[3] & 0xf0)==0xe0)
            {
                sprintf(buffer,"%03i.jpg",n);
                n++;
                FILE *img = fopen(buffer,"w");
            }
    }
    fclose(card);
}
