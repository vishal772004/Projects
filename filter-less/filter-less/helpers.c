#include "helpers.h"

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
    for(int i=0;i<height;i++)
    {
        for(int j=0;j<width;j++)
        {
            image[i][j].rgbtRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
            image[i][j].rgbtGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
            image[i][j].rgbtBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
        }
    }
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
