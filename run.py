import random

Player_One = []
Computer_Player = []
board = []
shots_taken = 1

"""
Board Function
"""
for i in range (0, 5):
    board.append(["0"]*5)

def random_row(board):
    return random.randint(0, len(board)- 1)

def random_col(board):
    return random.randint(0, len(board[0])- 1)

"""
Guess row and column function
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
            print(f"The great Battleships, are you ready for war! {user_name}!")
            return user_name
        else:
            print("please enter username here.")

username = get_username()           

def print_board(board):
    for row in board:
        print ("".join([col if col != "S" else "0" for col in row]))


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
                print ("You Must Enter A Number Between 0-4!")
                continue
            elif board[guess_row][guess_col] == "X":
                print("You Have Already Hit This Ship!")
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

def play_again():
   while True:
        play_game()
        restart = input('do you want to restart Y/N?')
        if restart == 'N':
            break
        elif restart == 'Y':
            continue
        print("Goodbye My Lover")
        return

play_game()
