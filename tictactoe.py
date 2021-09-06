"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    available = set()

    rowNum = 0
    elementNum = 0

    #Loops through board rows
    for row in board:

        elementNum = 0
        
        #Loops through elements in row
        for element in row:
            #If space is empty then the location is note
            if (element == EMPTY):
                available.add((rowNum, elementNum))
            elementNum += 1

        rowNum += 1

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #Creates deep copy of board
    newBoard = copy.deepcopy(board)
    row, column = action

    #Raises error if grid position is taken
    if (newBoard[row][column] != EMPTY):
        raise NameError("Action not valid")

    #Adds turn to grid
    newBoard[row][column] = player(newBoard)
    return newBoard

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


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """    

    #If there is a winner then returns True
    if (winner(board) != None):
        return True
    else:
        #If there is an empty cell then returns False
        for row in board:
            for element in row:
                if (element == EMPTY):
                    return False
        #Otherwise returns True
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1

    return 0

def minimax(board):
    
    """Returns the optimal action for the current player on the board.

    X max player
    O min player"""

    #Checks to see if game is over
    if (terminal(board)):
        return None

    #Gets current player    
    current = player(board)

    #Uses min/max value depending on current player
    if (current == X):                
        return max_value(board)[1]
    else:
        return min_value(board)[1]            

#Maximising function (for X)
def max_value(board):
    #Checks to see if game has ended (stopping condition)
    if (terminal(board) == True):
        return [utility(board), None]
    
    #Sets arbitrary lowest value
    v = -math.inf
    optimal = None

    #Loops through possible actions to find minimising value    
    for action in actions(board):
        value = min_value(result(board, action))[0]

        #If better path is find then it replaces current
        if (value > v):
            v = value
            optimal = action

            #If path with possible win is found then result is returned
            if value == 1:
                return [v, optimal]

    #Otherwise result is returned after iteration has concluded
    return [v, optimal]

#Minimising function (for O)
def min_value(board):
    #Checks to see if game has ended (stopping condition)
    if (terminal(board) == True):
        return [utility(board), None]

    #Sets arbitrary highest value
    v = math.inf
    optimal = None

    #Loops through possible actions to find minimising value
    for action in actions(board):
        value = max_value(result(board, action))[0]

        #If path with possible win is found then result is returned
        if (value < v):
            v = value
            optimal = action

            if value == -1:
                return [v, optimal]

    #Otherwise result is returned after iteration has concluded  
    return [v, optimal]
