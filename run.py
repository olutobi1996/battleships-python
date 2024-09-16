import random
import colorama
from colorama import Fore, Back, Style

colorama.init()

"""
Board Variable and Shots_Taken variable
"""
board = []
shots_taken = 1

"""
Board Function
"""
for i in range(0, 5):
    board.append(["0"] * 5)
"""
New Board Function
"""
def new_board():
    board = []
    for i in range(0, 5):
        board.append(["0"] * 5)
    ship_row = random_row(board)
    ship_col = random_col(board)

"""
Ships Positions
Ship 1
"""
def random_row(board):
    return random.randint(0, len(board) - 1)


def random_col(board):
    return random.randint(0, len(board[0]) - 1)


"""
Ship Row/Col varible for ship to be hit at random placements
"""
ship_row = random_row(board)
ship_col = random_col(board)

"""
Enter username function and welcome to battleships game
"""

def get_username():
    while True:
        user_name = input("Enter username here: ")
        if user_name:
            print(
                Fore.RED + f"The great Battleships, are you ready for war! {user_name}!"
            )
            return user_name
        else:
            print("please enter username here.")


username = get_username()

def print_board(board):
    for row in board:
        print(Back.GREEN + "".join([col if col != "S" else "0" for col in row]))

def create_ships():
    ships = 0
    while ships < 4:
        random_row = random.randint(0, grid_size - 1)
        random_col = random.randint(0, grid_size - 1)
        if boardoard[random_row][random_col] == '.':
            boardoard[random_row][random_col] = 'S'
            ships +=1

"""
Play Game function while loop including 
board range, how many ships left, if user has
hit a ship and print statment when they have won
"""
def play_game():
    ships_left = 1
    while ships_left > 0:
        print_board(board)
        while True:
            try:
                guess_row = int(input("Guess_Row, Enter number between 0-4>:"))
                guess_col = int(input("Guess_Col, Enter number between 0-4>:"))
            except ValueError:
                print("Invalid Number")
                continue
            if guess_row not in range(0, 5) and guess_col not in range(0, 5):
                print("You Must Enter A Number Between 0-4!")
                continue
            elif board[guess_row][guess_col] == "X":
                print("\033[31m" + "You Have Already Hit This Ship!")
                continue
            elif board[guess_row][guess_col] == "O":
                print("You Have Already Hit This Spot!")
                continue
            break
        if ship_row == guess_row and ship_col == guess_col:
            print("Bang, What A Hit! You Smashed My Ship")
            board[guess_row][guess_col] = "X"
            ships_left -= 1
        else:
            print("Unlucky You missed!")
            board[guess_row][guess_col] = "P"
    print("Congrats, you won!")

"""
Play Again function, including loop 
string for user to answer if they 
would like to play again
"""
def play_again():
    while True:
        play_game()
        restart = input("do you want to restart Y/N?")
        if restart == "N":
            break
        elif restart == "Y":
            continue
        print("Goodbye My Lover")
        return
play_again()

