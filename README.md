# Battleships-Python
Battleships-Python is a command-line interface game. To represent the board, i created the letter "O" to represent each table column and row. When someone makes a move, the CLI will tell me and a ship will display on the user/computer board. To fire a shot you use the "X" and aim using any number below the range of the columns and rows which is 5.


![Screenshot-pure-souls](https://github.com/olutobi1996/pure-souls/assets/169264552/9eca13f0-275d-4ec3-8659-40f1adb80f9b)

### Existing Features

To start the game you write "python3 run.py" and press Enter, after entered you will have "username" input and after entering username you will start the game. There will be one board displayed. The CLI was ask you to guess the column or row of the computers board and try and hit a ship. Once the shot has been taken the CLI will return a statement wether you have hit or missed. It will also display the computers board and where the shots you have taken.

Creating a new game
Once all the ships on either board have been hit, the  "if ship_row == guess_row and ship_col == guess_col:" function that calls where the ships are hit will run a loop and end the game if this is true. the console will print("Congrats, you won!"). You will be asked a question ('do you want to restart Y/N?') & if the response is Y, the play_again fucntion will start a new game if not the console will print("Goodbye My Lover").

Database
To store my python Battleships game i used Heroku for this project.

### Features Left to Implement

- Another feature idea for the future of the website is review section of Pure Soul class members who talk about there positive experience and also any negative experiences they found when meditating or doing yoga, this will be provided in short video clips in a Q&A styled format.

- Also spoke about above was adapting different types of classes down the line, i.e hot yoga and also branching out into sound healing depending on feedback from users and members.

## Testing 

- The website has been tested numerous times to make sure the user has an easy and enjoyable experience.

## Navigation Bar 
- Starting with the navigation bar, this section is for the user to navigate the pages easy, at first i struggled with the links to different sections of the page as i was using the id i created at the wrong section of my page, this made the broswser go to different sections. I also found difficulty with how to add the IDs to anchor i couldnt work out why when i clicked the different sections of the nav, that it wouldnt work. 

- I placed the navigation bar just off the centre to the right and i used display flex & wrap elements to make it responisve when viewed on different devices.

## First Image 
- Below the nav we have the first image. I used an enlarged picture that captures the details of the image so the user has a positive feeling when viewing this photo. 

- One main problem i had was being able to adjust the wdith and height when the image was viewed on a smaller device and keeps its full size. I overcame this problem by adding width to 100% and media queries so when it was viewed on smaller device you could still see the full image just smaller.

## In Depth 
- Below the first image we have a three vertical column layout, this was provide asthetically for the user as i wanted to give the user the choice of seeing each section of information next to each other instead of potentially being dis-interested by scrolling past each part. I also changed the color of the headings in comparison to the text below to let the user know what each section means. 

- Adding the vertical column layout i first tried using float styling which did not respond when adding other elements in, so i changed it to using display flex which i had a great time with.

I  used display flex & wrap elements to make each section stack on top of each other when viewed on a phone and different devices to make it responsive.

## Second Image

- Below the three vertical column we have the second image. I used an enlarged picture also in this section that gives the user more inspiration when scrolling through the page. I also liked the colours of the picture as bright orange catches your eye and is good visually for the user. 

- Again main problem i had was being able to adjust the wdith and height when the image was viewed on a smaller device and keeps its full size. I overcame this problem by adding width to 100% and media queries so when it was viewed on smaller device you could still see the full image just smaller.

## Classes
- Below the second image we have a two vertical column layout, this was provide asthetically for the user as i wanted to give the user the choice of seeing each section of information next to each other instead of potentially being dis-interested by scrolling past each part. I also changed the color of the headings in comparison to the text below to let the user know what each section means. I also kept the consistency of having the vertical layout below each image for the user to enjoy there experience smoothly.

- Adding the vertical column layout i first tried using float styling which did not respond when adding other elements in, so i changed it to using display flex which i had a great time with.

I  used display flex & wrap elements to make each section stack on top of each other when viewed on a phone and different devices to make it responsive.

## Video
 - Below classes i had a video section, this was provided so the user could have some extra information for a well known figure in the meditative and yoga realm. This was again to encourage and help users to seek more about the benefits and how you do both these excercies, the video does not play automatically so the user has a choice.

 - This i fine easy as i was able to copy link onto my code so didnt have difficulty when facing this element.

 - I set the attributes of the video to width and height of 300px so when viewed on a phone it does not change it is already the correct height and width.

## Sign Up

- This part of a page is a necessity as this allows users to directly contact pure souls and we can provide emails, texts and phone calls to speak with anyone interested. I thought it would be good place towards end of the page as this allows users to make a final decision wether it is for them or not.
- This i found fine as i was able to use inspiration from my love running project previously.

 - I  used display flex & wrap elements to make sign up section rsponsive when veiwed on other devices and it kept a clear view of what it was stating.

## Days Location Time

- This part of a page is a necessity as this allows users to see the days time and location of when these classes are on. I thought it would be good place towards end of the page as this allows users to make a final decision wether it is for them or not.

- I had spent a few hours trying to figure out how to style my table without a border and also i had one to many columns on my table so it wasnt showing up in the browser correctly. After figuring out where to put which element and what style to use it was placed nicely on the broswer.
- I  used display flex & wrap elements to make day/time/location section rsponsive when veiwed on other devices and it kept a clear view of what it was stating.

## Footer
- This part of a page is a vital as this allows users to see our social media pages. I thought it would be good place towards end of the page as this allows users to make a final decision wether they would like to follow our social media pages or not.

- The only problem i had with the footer was through jigsaw validator for days it was saying there was a problem as i had the tag outside the body element so i had to move it within this element, after that was solved i had no further issues.

-I  did not have to use any resposive styles as the footer is small favcions in the corner of the page that stay in the same place when viewed on a smaller device.
### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator]https://validator.w3.org/nu/?doc=https%3A%2F%2Folutobi1996.github.io%2Fpure-souls%2F 
- CSS
  - No errors were found when passing through the official [(Jigsaw)]https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Folutobi1996.github.io%2Fpure-souls%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=envalidator#warnings)

### Unfixed Bugs
There were no unfixed bugs in the final code but for days i had W3C validator show i had a "parse erorr" problem with my footer tag. For days i spent trying to solve problem on my own by using google and looking back through the project "love running", but still had no luck. So in the end with help from my tutor and slack team we solved the problem, it was simple error of putting footer tag within the body tag.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
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