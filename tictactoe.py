"""
Tic Tac Toe Player
"""

import math

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
    if any(None in row for row in board):
        XCount = sum(row.count("X") for row in board)
        OCount = sum(row.count("O") for row in board)
    if XCount == OCount:
        return "X"
    else:
        return "O"


def actions(board):
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    i, j = action
    if i < 3 and j < 3 and board[i][j] is EMPTY:
        playername = player(board)
        new_board = board
        new_board[i][j] = playername
        return new_board
    else:
        raise Exception("Invalid")


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return "X"
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return "O"
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == "X":
            return "X"
        elif board[0][j] == board[1][j] == board[2][j] == "O":
            return "O"

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == "X":
        best_val = -1
        best_move = (-1. -1)
        c = sum(row.count(EMPTY) for row in board)
        if c == 9:
            return best_move
        for action in actions(board):
            move_value = min_value(result(board, action))
            if move_value == 1:
                best_move = action
                break
            if move_value > best_val:
                best_move = action
        return best_move
    elif player(board) == "O":
        best_val = 1
        best_move = (-1, -1)
        for action in actions(board):
            move_value = max_value(result(board, action))
            if move_value == -1:
                best_move = action
                break
            if move_value > best_val:
                best_move = action
        return best_move


def min_value(board):
    value = 99
    for action in actions(board):
        v = min(value, max_value(result(board, action)))
        if v == -1:
            break
        return v


def max_value(board):
    value = -99
    for action in actions(board):
        v = max(value, min_value(result(board, action)))
        if v == 1:
            break
        return v