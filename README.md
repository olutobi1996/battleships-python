# Battleships-Python
Battleships-Python is a command-line interface game. To represent the board, i created the letter "O" to represent each table column and row. When someone makes a move, the CLI will tell me and a ship will display on the user/computer board. To fire a shot you type any number below the range of the columns and rows which is 5 and if you hit a ship it will show "X" on the board and if you miss it will show "M". I built the board by creating  a "board = []" varible and then creating the range of rows and columns using this function. "for i in range (0, 5): board.append(["0"]*5)"


![alt text](<Screenshot 2024-09-13 203258-1.png>)

### Existing Features

To start the game you run "python3 run.py" in the CLI and press Enter, after entered you will have "username" input and after entering username you will start the game. There will be one board displayed. The CLI was ask you to guess the column or row of the computers board and try and hit a ship. Once the shot has been taken the CLI will return a statement wether you have hit or missed. It will also display the computers board and where the shots you have taken. I created the username by printing a string statement to the console def get_username(): "print(Fore.RED + f"The great Battleships, are you ready for war! {user_name}!")", i also used a while loop to make sure the user entered in a correct username.

Also within the battle ships game you will be notified on the board when you have missed with the letter "M" showing on the board.
Also you will have an "X" show up on the board when you have hit the ship, there are 4 ships to take down during the game, at the end of the game you will be notified by the game that you won and how many shots it took you. I created this by using a string statement in my play game function, and also a loop for when you take each shot and what it returns if you hit, miss or write a number outside the range.

![alt text](<Screenshot 2024-09-18 190257.png>)

![alt text](<Screenshot 2024-09-13 203315-1.png>)

Creating a new game
Once all the ships on either board have been hit, the  "if ship_row == guess_row and ship_col == guess_col:" function that calls where the ships are hit will run a loop and end the game if this is true. the console will print("Congrats, you won!"). You will be asked a question ('do you want to restart Y/N?') & if the response is Y, the play_again fucntion will start a new game if not the console will print("Goodbye My Lover").

![Creating new game](<Screenshot 2024-09-15 170451.png>)

Colorama
I Have also imported colorama into the run.py file, this has allowed me to style the battleships game board for the user making it visually enjoyable, i have also styled the username red by coloring the text red, this is also for the slight affect for the user making it a bit vissually interesting.
![Colorama](<Screenshot 2024-09-13 204648.png>)  ![Colorama](<Screenshot 2024-09-13 204725.png>)


### Features Left to Implement

- Another feature idea that i want to add in the future is a multiplayer game where you can play two users against the computer.
- I also would like to expand the rows and columns of the board with more ships to be taken down.

## Testing 

- The website has been tested numerous times to make sure the game runs smoothly, i also had a friend and my tutor test the game out on other computers to make sure.
- Also within the game there are functions that test if the user has input something incorrect, i.e i created the board columns and rows to be within 5 by 5, so if the user his numbers outside this range there will be a message to say ""Invalid Number". I created this by using a loop to make sure the user enters a correct number and the loop will continue until they have done so.
-I also created within the loop a "elif board[guess_row][guess_col] = print("You Have Already Hit This Spot!") continue" so if the user has already hit a ship they will have a message pop up saying "You Have Already Hit This Spot!".


### Validator Testing 
https://pep8ci.herokuapp.com/#
![](<Screenshot 2024-09-13 205617.png>)

I Also tested my code by running it through the CI Python Linter which is a website that checks your python code for any errors. When i first pasted my code into the terminal ther were some whitespace errors and print statments and functions, i also ran into some character errors where some of my text was too long. I fixed this by shortening my text and also clearing the whitespace, upon doing this it ran through the terminal with no errors as you can see above with the picture and link.

### Unfixed Bugs
There were no unfixed bugs but for a long time i had a challenge with adding more ships to the board, i spent many hours trying to figure out how to add more then one ship as everytime i would try a new function for the ships or extend the board size and try putting the ships into a class the code would break. This was my most challenging part of this project, apart from that i found writing the loop statements for the board functions and also defining variables i created along with importing colorama and adding styling go pretty smooth, by the end of the project after testing it various times and also with friends it had no bugs.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- To store my python Battleships game i used Heroku for this project. The steps to deploy are as follows: 

  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the main branch
  - Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits & Media

-Alot of the code was from knowledge that has been aquired over the python module

- Some help from https://www.w3schools.com/python/ for correct syntax.

- There was also some help from https://stackoverflow.co/teams/ for function ideas.