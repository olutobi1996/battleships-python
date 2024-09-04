import random

def get_username():
    while True:
        user_name = input("Enter username here: ")
        if user_name:
            print("Welcome to the great Battleships game, are you ready for war! {user_name}!")
            return user_name
        else:
            print("please enter username here.")

board = []
for i in range (0, 5):
    board.append(["0"]*5)
    print(board)

    def print_board(board):
        for row in board:
            print "".join(row)

    print_board(board)

    def random_row(board)
    return randint(0, len(board)- 1)
    def random_col(board)
    return randint(0, len(board[0])- 1)



Player_One = []
Computer_Player = []


new_game()
