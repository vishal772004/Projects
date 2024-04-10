MOVIE MANIA
Video Demo:https://youtu.be/YkIrT1NcHEo
Description:
Welcome to Movie Mania which suggests the user good movies which is in the top 250 imdb ratings in the imdb website.To begin with the code first I have downloaded IMBDTop250.csv from github . Then used the template given by cs50 and started coding. I have imported four libraries namely re i.e regular expressions library ,sys library , csv library and random library .

So in the main function I am printing the list of ways to find the movie or to suggest a movie based on that parameter . The first parameter was  based on rating of a particular movie from the csv file . The second parameter was suggesting movies based on the genre . The third parameter was based on the year of release of a movie . The fourth parameter was based on the main actors of the movie . The fifth parameter was based on the language of the  movie . The sixth parameter was just random movie suggestion . I have used choice variable to get the option that the user has chosen and passed it to the match case statement . For every case there is a function called and at the end for any invalid choice given by the user I have prompted the user to give a valid input once again , if the user fails to give a proper choice the program exits.

Then there is a very important function that uses csv library named csv_Reader() which reads  the IMDBTop250.csv using a DictReader and stores it into a list and returns the list whenever it is called and every function except option1() function calls this function.

In a function called Rating() , first I have called csv_Reader() and stored the list that is returned in a variable called row . Then I have used list comprehension which was explained in the last week of cs50 and extracted out ratings and movie name in a separate list . Then I have used two while loops where the first one to iterate through the whole row and the second one to print only ten movies at a time so that it is not conjested . Then this function prints the top 10 movies according to its rating and it will ask the user if he wants the next 10 movies . Depending on the answer he will get another 10 movies printed on the screen and if he types no the program exits using sys.exit() function .

In the next function called genre() it gives the user a list of genres of which the user can choose and enter his choice . Then a match case statement is used where  in each case another function named genres() is called giving the case or option number as argument to the function genres() .

In the function genres() which takes the option number as an argument and uses two list for storing genres and movie name . Then we again make use of those two loops but this time there is an if condition that checks a function named option1() which is called in the if statement that returns true or none . Then it prints those movies that is of that genre  .

In the function option1() that takes two arguments namely the option number of genre() function and individual genre from the list . An if condition using re.search searches for a pattern that is genre inside that genre from the list . If it is found the function returns true and if not found nothing is returned .

In the function called year() contains list of the year of the movie release and the movie name .Then it asks the user to enter a year .Then it checks that if there are any movies released that year and if there are any movies it will print those movies .

In the function called random_movie() , random library is used and random.randint() function is used that gives any random movie from the list of top 250 movies .

This was my CS50 Final Project for Introduction To Python for the Year 2024 .
Hope you like it!!
Thank You.


