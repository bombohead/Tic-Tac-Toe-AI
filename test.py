"""
Tic Tac Toe Player
"""

import math

def player(board):
    """
    Returns player who has the next turn on a board.
    """

    count = 0

    #Loops through board rows
    for row in board:
        #Loops through elements in row
        for element in row:
            if (element == X) or (element == O):
                count += 1

    #If there are an even number of turns played then
    #it is X's turn
    if (count % 2) == 0:
        return X
    #Otherwise it is O's turn
    else:
        return O

EMPTY=None

X="X"
O="O"

board = [[EMPTY, EMPTY, X],
        [X, EMPTY, X],
        [X, EMPTY, X]]

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    winner = None

    #Checks horizontal wins
    for row in board:
        if (row[0] == X) and (row[1] == X) and (row[2] == X):
            winner = X
        elif (row[0] == O) and (row[1] == O) and (row[2] == O):
            winner = O

    #Checks vertical wins
    for y in range(0,3):
        if (board[0][y] == X) and (board[1][y] == X) and (board[2][y] == X):
            winner = X
        elif (board[0][y] == O) and (board[1][y] == O) and (board[2][y] == O):
            winner = O

    #Checks diagonal wins
    if (board[0][0] == X) and (board[1][1] == X) and (board[2][2] == X):
        winner = X
    elif (board[0][0] == O) and (board[1][1] == O) and (board[2][2] == O):
        winner = O
    elif (board[0][2] == X) and (board[1][1] == X) and (board[2][0] == X):
        winner = X
    elif (board[0][2] == O) and (board[1][1] == O) and (board[2][0] == O):
        winner = O

    return winner

