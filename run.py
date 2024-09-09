import random

Player_One = []
Computer_Player = []
board = []

"""Board Function
"""
for i in range (0, 5):
    board.append(["0"]*5)

def random_row(board):
    return random.randint(0, len(board)- 1)

def random_col(board):
    return random.randint(0, len(board[0])- 1)


def get_username():
    while True:
        user_name = input("Enter username here: ")
        if user_name:
            print("Welcome to the great Battleships game, are you ready for war! {user_name}!")
            return user_name
        else:
            print("please enter username here.")

"""
Board Function
"""
board = []
for i in range (0, 5):
    board.append(["0"]*5)
print(board)

def print_board(board):
        for row in board:
            print ("".join(row))

print_board(board)

"""
    Guess row and column function
     """
ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(input("Guess_Row, Enter number between 0-5>:"))
guess_col = int(input("Guess_Col, Enter number between 0-5>:"))

def play_game():

    if guess_row == ship_row and guess_col == ship_col:
        print("Congrats You Took My Ship Down!")
    else:
        print("Unlucky You missed!")
        except ValueError:
        ("Only Enter A Number!")

        if guess_row (0-5) and guess_col not in range (0-5):
            print ("You Must Enter A Number Between 1-5!")
            if: board [row] == "X" or board [col] == "X":
                print("You Have Already Hit This Ship!")
                continue
            elif: (row, column) == guess_col or (row, column) == guess_row:
            print("Bang, What A Hit! You Smashed My Ship")
            board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("Congrats, you won!")
                new_game()

            def play_again():
                again = str(input("Do you want to play again? (type yes or no): "))
            if again == "yes":
                else
                print("Goodbye My Lover")
                return

    

new_game()
