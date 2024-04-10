MOVIE MANIA
Video Demo:
Description:
Welcome to Movie Mania which suggests the user good movies which is in the top 250 imdb ratings in the imdb website.To begin with the code first I downloaded IMBDTop250.csv from github . Then used the template given by cs50 and started coding. I have imported four libraries namely re i.e regular expressions library ,sys library , csv library and random library .

So in the main function I am printing the list of ways to find the movie or to suggest a movie based on that parameter . The first parameter was  based on rating of a particular movie from the csv file . The second parameter was suggesting movies based on the genre . The third parameter was based on the year of release of a movie . The fourth parameter was based on the main actors of the movie . The fifth parameter was based on the language of the  movie . The sixth parameter was just random movie suggestion . I have used choice variable to get the option that the user has chosen and passed it to the match case statement . For every case there is a function called and at the end for any invalid choice given by the user I have prompted the user to give a valid input once again , if the user fails to give a proper choice the program exits.


