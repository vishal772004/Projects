#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    double avg;
    for(int i=0;i<height;i++)
    {
        for(int j=0;j<width;j++)
        {
            avg = (image[i][j].rgbtRed+image[i][j].rgbtBlue+image[i][j].rgbtGreen)/3.0;
            avg = round(avg);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
