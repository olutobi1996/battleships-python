import random

def get_username();
    while True:
        user_name = input("Enter username here: ")
        if user_name:
            print("Welcome to the great Battleships game, are you ready for war! {user_name}!")
            return user_name
        else:
            print("please enter username here.")
        


Player_One = []
Computer_Player = []

board = []
for i in range (0, 5):
    board.append(["0"]*5)
    print(board)

new_game()
