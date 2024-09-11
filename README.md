# Battleships-Python
Battleships-Python is a command-line interface game. To represent the board, i created the letter "O" to represent each table column and row. When someone makes a move, the CLI will tell me and a ship will display on the user/computer board. To fire a shot you use the "X" and aim using any number below the range of the columns and rows which is 5.


![Screenshot-pure-souls](https://github.com/olutobi1996/pure-souls/assets/169264552/9eca13f0-275d-4ec3-8659-40f1adb80f9b)

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


### Content 

- The icons in the Header were taken from [Font Awesome](https://fontawesome.com/)
- The text for in-depth & techniques was knowledge from over the years.
- how to style the layout of column layout was isnpired by https://www.w3schools.com/
- Instructions on how to implement form validation & how to write the html code was on the Sign up form was taken from  
 inspiration from my [Love Running Project]
 - Table format was inspired by (https://codeinstitue.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- Both of the photos used on the page are used from https://www.pexels.com/
- This site is a free image website

- 'How to meditate for beginners' was taken from (https://www.youtube.com/) 
- I clicked on the video and below the video there was a share button i then copied the code.