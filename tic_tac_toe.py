'''
Assignment Name: W02 Prove: Tic-Tac-Toe
Author: Isaias Monzon
'''

import json

# These are the characters used in the board.
X = 'X'
O = 'O'
BLANK = ' '


def read_board(filename):
    '''Read the previously existing board from the file if it exists'''
    with open(filename, "w+") as file:
        blank_board_data = {
            "board": [" ", " ", " ", " ", " ", " ", " ", " ", " "]}
        board_formated = blank_board_data
        json.dump(board_formated, file)


def save_board(filename, board):
    '''Save the current game to a file'''
    with open(filename, "w+") as file:
        board_formatted = {"board": board}
        json.dump(board_formatted, file)
        print("Game saved!")
    quit()


def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen'''
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def is_x_turn(board):
    '''Determine whose turn it is'''
    x_count = 0
    o_count = 0
    for i in board:
        if i == "X":
            x_count += 1
        if i == "O":
            o_count += 1
    if x_count <= o_count:
        return True
    else:
        return False


def main(board):
    '''Play the game of Tic-Tac-Toe'''
    turn = is_x_turn(board)
    duplicate = True
    while duplicate:
        if turn == True:
            print("It is X's turn!")
            player_name = "X"
        if turn == False:
            print("It is O's turn!")
            player_name = "O"
        position = input("Where would you like to play?: ")
        if position.upper() == "Q":
            save_board(filename, board)
        position = int(position)
        if board[position - 1] == " ":
            board_data[position - 1] = player_name
            duplicate = False
        else:
            print("This position is not empty, try a different one")
        display_board(board)


def game_done(board):
    '''Determine if the game is finished'''

    # The game is finished if someone has completed a row.
    for row in range(3):
        if (board[row * 3] != BLANK and board[row * 3]
                == board[row * 3 + 1] == board[row * 3 + 2]):
            print("The game was won by", board[row * 3])
            return True

    # The game is finished if someone has completed a column.
    for col in range(3):
        if (board[col] != BLANK and board[col]
                == board[3 + col] == board[6 + col]):
            print("The game was won by", board[col])
            return True

    # The game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        print("The game is a tie!")
        return True

    return False


# Display how the game is to be played
print("Enter a number from 1 to 9 to play. Enter 'q' to save your game")
print("The following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# Create a save file if there is none
filename = "save_game.json"

file_created = False
while file_created == False:
    try:
        with open(filename, "r+") as save_file:
            saved_data = json.load(save_file)
            board_data = saved_data["board"]
            display_board(board_data)
            file_created = True
    except:
        with open(filename, "w+") as f:
            blank_board_data = {
                "board": [" ", " ", " ", " ", " ", " ", " ", " ", " "]}
            json.dump(blank_board_data, f)

game_finished = False
while game_finished == False:
    main(board_data)
    game_finished = game_done(board_data)

# reset the game once finished
read_board(filename)
