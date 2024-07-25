#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    double avg=0;
    for(int i=0;i<height;i++)
    {
        for(int j=0;j<width;j++)
        {
            avg = (image[i][j].rgbtRed+image[i][j].rgbtBlue+image[i][j].rgbtGreen)/3.0;
            avg = round(avg);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    double sepiaRed,sepiaGreen,sepiaBlue;
    for(int i=0;i<height;i++)
    {
        for(int j=0;j<width;j++)
        {
            sepiaRed =round( .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            if (sepiaRed>255)
                sepiaRed = 255;
            if(sepiaGreen>255)
                sepiaGreen = 255;
            if(sepiaBlue>255)
                sepiaBlue = 255;

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen =  sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int copy;

    for(int i=0;i<height;i++)
    {
        for(int j=0;j<width/2;j++)
        {
            RGBTRIPLE temp = image[i][width-j];
            image[i][width-j] = image[i][j];
            image[i][j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    for (int i=0;i<height;i++)
    {
        for (int j=0;j<width;j++)
        {
            int n=0;
            double ravg,bavg,gavg=0.0;
            int rsum=0,gsum=0,bsum=0;
           for (int rows=0;rows<3;rows++)
           {
                for(int col=0;col<3;col++)
                {
                    if((i-1)<0 || (i+1)>height)
                        continue;
                    if((j-1)<0 || (j+1)>width)
                        continue;

                rsum += image[rows][col].rgbtRed;
                bsum += image[rows][col].rgbtBlue;
                gsum += image[rows][col].rgbtGreen;
                n++;
                }
            }
            ravg = round(rsum/n);
            bavg = round(bsum/n);
            gavg = round(gsum/n);

            image[i][j].rgbtRed = ravg;
            image[i][j].rgbtGreen = gavg;
            image[i][j].rgbtBlue = bavg;

        }
    }


    return;
}
