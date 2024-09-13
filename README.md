# Battleships-Python
Battleships-Python is a command-line interface game. To represent the board, i created the letter "O" to represent each table column and row. When someone makes a move, the CLI will tell me and a ship will display on the user/computer board. To fire a shot you use the "X" and aim using any number below the range of the columns and rows which is 5.


![Python-BattleShips-Game]()

### Existing Features

To start the game you write "python3 run.py" and press Enter, after entered you will have "username" input and after entering username you will start the game. There will be one board displayed. The CLI was ask you to guess the column or row of the computers board and try and hit a ship. Once the shot has been taken the CLI will return a statement wether you have hit or missed. It will also display the computers board and where the shots you have taken.

Creating a new game
Once all the ships on either board have been hit, the  "if ship_row == guess_row and ship_col == guess_col:" function that calls where the ships are hit will run a loop and end the game if this is true. the console will print("Congrats, you won!"). You will be asked a question ('do you want to restart Y/N?') & if the response is Y, the play_again fucntion will start a new game if not the console will print("Goodbye My Lover").


### Features Left to Implement

- Another feature idea that i want to add in the future is a multiplayer game where you can play two users against the computer.
- I also would like to expand the rows and columns of the board with more ships to be taken down.

## Testing 

- The website has been tested numerous times to make sure the game runs smoothly, i also had a friend and my tutor test the game out on other computers to make sure.


### Validator Testing 


### Unfixed Bugs
There were no unfixed bugs in the final code but for days i had W3C validator show i had a "parse erorr" problem with my footer tag. For days i spent trying to solve problem on my own by using google and looking back through the project "love running", but still had no luck. So in the end with help from my tutor and slack team we solved the problem, it was simple error of putting footer tag within the body tag.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- To store my python Battleships game i used Heroku for this project. The steps to deploy are as follows: 

  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the main branch
  - Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

-Alot of the code was from knowledge that has been aquired over the python module.


### Content 


### Media

- Some help from https://www.w3schools.com/python/ for correct syntax.

- There was also some help from https://stackoverflow.co/teams/ for function ideas.