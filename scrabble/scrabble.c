#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>

int score(string s);

int main(void)
{
    string player_1 = get_string("Player 1:");
    string player_2 = get_string("Player 2:");

    int score1 = score(player_1);
    int score2 = score(player_2);
    if (score1>score2)
    {
        printf("Player 1 Wins!");
    }
    else if(score2>score1)
    {
        printf("Player 2 Wins!");
    }
    else
    {
        printf("Tie!");
    }
    printf("\n");
}

int score(string s)
{
    int points[] ={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    int scoreboard = 0;
    for (int i=0,n=strlen(s);i<n;i++)
    {
        int value = toupper(s[i])-65;
        scoreboard +=points[value];
    }
    return scoreboard;
}
