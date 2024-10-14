import random
import colorama
from colorama import Fore, Back, Style


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

"""
New Board Function
"""
def new_board():
    board = []
    for i in range(0, 5):
        board.append(["0"] * 5)
    return board

def print_board(board):
    for row in board:
        print(Back.GREEN + "".join([col if col != "S" else "0" for col in row]))

def create_ships(board):
    ships = 0
    while ships < 4:
        random_row = random.randint(0, len(board) - 1)
        random_col = random.randint(0, len(board[0]) - 1)
        if board[random_row][random_col] == "0":
            board[random_row][random_col] = 'S'
            ships +=1

"""
Play Game function while loop including
board range, how many ships left, if user has
hit a ship and print statment when they have won
"""
def play_game():
    ships_left = 4
    shots_taken = 0
    board = new_board()
    create_ships(board)
    while ships_left > 0:
        print_board(board)
        while True:
            try:
                guess_row = int(input("Guess_Row, Enter number between 0-4>:"))
                guess_col = int(input("Guess_Col, Enter number between 0-4>:"))
            except ValueError:
                print(Fore.RED + "Invalid Number")
                continue
            if guess_row not in range(0, 5) or guess_col not in range(0, 5):
                print(Fore.RED + "You Must Enter A Number Between 0-4!")
                continue
            elif board[guess_row][guess_col] == "X":
                print(Fore.RED + "You Have Already Hit This Ship!")
                continue
            elif board[guess_row][guess_col] == "M":
                print(Fore.RED + "You Have Already Hit This Spot!")
                continue
            break
        if board[guess_row][guess_col] == "S":
            print("Bang, What A Hit! You Smashed My Ship")
            board[guess_row][guess_col] = "X"
            ships_left -= 1
        else:
            print(Fore.RED + "Unlucky You missed!")
            board[guess_row][guess_col] = "M"
        shots_taken += 1

    print_board(board)
    print(f"Congrats, you won! You needed {shots_taken} shots")

"""
Play Again function, including loop
string for user to answer if they
would like to play again
"""
def play_again():
    while True:
        play_game()
        restart = input("do you want to restart Y/N?")
        if restart.lower() == "n":
            print("Goodbye My Lover")
            return
play_again()

