

from ai import MODEL
from ai import strategy_dumb
from ai import strategy_oracle
from ai import strategy_random

#!/usr/bin/python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.

#    ____          _            ______
#   / __/__  ___ _(_)__  ___   /_  __/__ ___ ___ _
#  / _// _ \/ _ `/ / _ \/ -_)   / / / -_) _ `/  ' \
# /___/_//_/\_, /_/_//_/\__/   /_/  \__/\_,_/_/_/_/
#          /___/

from time import sleep


CPU_DELAY = 0.75

def logo(): # Module Interface
    """Display the game's colorful logo"""
    print()
    print(red('888888888               '), white('888888888                '), cyan('888888888                 '))
    print(red('"8888888" ooooo  ooooo  '), white('"8888888" ooo     ooooo  '), cyan('"8888888"  ooo    ooooo   '))
    print(red('   888     888  88   8  '), white('   888    888    88   8  '), cyan('   888   88   88  8       '))
    print(red('   888     888  88      '), white('   888   8ooo8   88      '), cyan('   888   88   88  8ooooo  '))
    print(red('   888     888  88    88'), white('   888  888  888 88    88'), cyan('   888   88o  88 o88      '))
    print(red('   888    88888  888888"'), white('   888  888  888  888888"'), cyan('   888   "888888 888888888'))
    print("                                                            ", "by ", yellow("DuckieCorp"), "(tm)", sep='')
    print(green("\nWOULD YOU LIKE TO PLAY A GAME?\n"))


def show(board): # Module Interface
    """
    Display the Tic-Tac-Toe board on the screen, in color

    When the optional parameter 'clear' is True, clear the screen before printing the board
    """
    if board:
        print(" {} | {} | {}\n---+---+---\n {} | {} | {}\n---+---+---\n {} | {} | {}\n".format(
            color(board[0][0]), color(board[0][1]), color(board[0][2]),
            color(board[1][0]), color(board[1][1]), color(board[1][2]),
            color(board[2][0]), color(board[2][1]), color(board[2][2])))


def get_human_move(board, letter): # Module Interface
    """
    Ask a human which move to take, or whether they want to quit.
    Perform rudimentary input validation, repeating the prompt until a valid
    input is given:
     * Integers must be in the range of [1..9] (whether it represents a legal
       move is to be handled by the caller)
     * Strings beginning with 'Q' or 'q' quit the game

    Return an integer [1..9] to indicate the move to take, or False to quit the game
    """
    while True:
        show(board)
        choice = input("Place your '{}' (or 'Q' to quit)> ".format(color(letter)))
        if not choice.isdigit():
            if choice.lower().startswith('q'):
                return False
            else:
                print("I don't understand '{}', try again!\n".format(choice))
        else:
            choice = int(choice)
            if not 0 < choice < 10:
                print("Numbers must be between 1 and 9, try again!\n")
            else:
                return choice


def player_select(): # Module Interface 
    while True:
        print("0)", red("X"), green("CPU  "), "vs.", cyan("O"), green("CPU"))
        print("1)", red("X"), white("Human"), "vs.", cyan("O"), green("CPU"))
        print("2)", red("X"), green("CPU  "), "vs.", cyan("O"), white("Human"))
        print("3)", red("X"), white("Human"), "vs.", cyan("O"), white("Human"))
        p = input("Choose game mode [0-3] or Q to quit > ")
        if p == "0" or p == "1" or p == "2" or p == "3":
            return int(p)
        elif p.lower() == "joshua":
            return 4
        elif p.lower().startswith('q'):
            return p
        else:
            print("\nInvalid selection!\n")


def make_board(): # Module Interface
    """
    A board is a 3-tuple of 3-tuples, where each tuple is one row
    """
    return tuple([tuple([1, 2, 3]),
                  tuple([4, 5, 6]),
                  tuple([7, 8, 9])])


def place(board, position, player): # Module Engine
    """
    Accepts: a game board (tuple), position (integer), and a player's identity ("X" or "O")
    Return a copy of the board with that player's mark put into the requested
    position, iff a player's mark isn't already present there.

    Otherwise, return False
    """
    if not 1 <= position <= 9:
        # player requested an out-of-bounds position
        return False

    # convert position into (row, col) coordinates
    row, col = pos_to_rowcol(position)

    if board[row][col] != 'X' and board[row][col] != 'O':
        # construct a brand new board
        new = []
        for r in board:
            new.append(list(r))
        new[row][col] = player
        # Always maintain the board as a tuple to guarantee that it
        # can never be accidentally modified
        return tuple([tuple(new[0]), tuple(new[1]), tuple(new[2])])
    else:
        return False


def horizontal_winner(board): # Module Engine
    """
    Determines which player has won a game with a horizontal triple.
    Input: a 2D game board.
    Return: 'X' or 'O' when there is a winner, or False when no player has 3 in
    a horizontal row

    The code we arrived at borders on being too clever for our own good, and
    bears some explanation.

    The first line checks whether the three cells in the top row are all the
    same.  This is ONLY true when the same player has played their mark there.
    The `and` conjunction at the end of each sub-clause might look useless, but
    is very important.  It returns the letter of the winning player:
        https://docs.python.org/3/reference/expressions.html#boolean-operations

    Without it, this function could only return 'True' or 'False', merely
    indicating that SOMEBODY won the game instead of stating who the winner is.
    """
    return (board[0][0] == board[0][1] == board[0][2] and board[0][2]) \
        or (board[1][0] == board[1][1] == board[1][2] and board[1][2]) \
        or (board[2][0] == board[2][1] == board[2][2] and board[2][2])


def vertical_winner(board): # Module Engine
    """
    Determines which player has won a game with a vertical triple
    """
    return (board[0][0] == board[1][0] == board[2][0] and board[2][0]) \
        or (board[0][1] == board[1][1] == board[2][1] and board[2][1]) \
        or (board[0][2] == board[1][2] == board[2][2] and board[2][2])


def diagonal_winner(board): # Module Engine
    """
    Determines which player has won a game with a diagonal triple
    """
    return (board[0][0] == board[1][1] == board[2][2] and board[2][2]) \
        or (board[2][0] == board[1][1] == board[0][2] and board[0][2])


def winner(board): # Module Engine
    """
    Returns the winner of the game (if any), or False when there is no winner
    """
    return horizontal_winner(board) or vertical_winner(board) or diagonal_winner(board)

 
def human_turn(board, letter): # Moduel Engine
    """
    Return False if the game is over,
           True to keep playing
    """
    while True:
        choice = get_human_move(board, letter)
        if choice is False:
            return False
        new_board = place(board, choice, letter)
        if not new_board:
            if letter == 'X':
                print(red("You can't play at {}!".format(choice)))
            else:
                print(cyan("You can't play at {}!".format(choice)))
        else:
            return new_board


def cpu_turn(board, letter, strategy, verbose=True): # Module Engine
    if letter == "X":
        color = red
    else:
        color = cyan
    if verbose:
        print(color("CPU {} is taking its turn...".format(letter)), end=' ', flush=True)
    sleep(CPU_DELAY)
    choice = strategy(board)
    if verbose:
        print(color("playing on {}\n".format(choice)))
    return place(board, choice, letter)


def pos_to_rowcol(position): # Module Engine
    """
    Given a TicTacToe board position (int),
    Return a tuple(row, col)

    Inverse of the function rowcol_to_pos()
    """
    cell = position - 1
    row = cell // 3
    col = cell % 3
    return row, col


def rowcol_to_pos(rowcol): # Module Engine
    """
    Given a row and column (as a tuple)
    Return a TicTacToe board position (int)

    Inverse of the function pos_to_rowcol()
    """
    row = rowcol[0]
    col = rowcol[1]
    pos = row * 3 + col
    return pos + 1


def open_cells(board): # Redundent Delete Later
    """ Returns a tuple of the unmarked cells in a Tic-Tac-Toe board """
    openings = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 'X' and board[row][col] != 'O':
                # convert (row,col) into a number
                openings.append(rowcol_to_pos(tuple([row, col])))
    return tuple(openings)


def first_open_cell(board): # Redundent
    """ Return the ID of the first unmarked cell in a Tic-Tac-Toe board """
    cells = open_cells(board)
    if cells != []:
        return cells[0]
    else:
        return None


def full(board): # Module Engine
    return open_cells(board) == ()


def keep_playing(board): # Module Engine
    """
    Accepts a board or False as input
           board: take another turn
           False: the user has requested to quit the game
    Return False if the game is over for any reason (quitting, win, lose or draw),
           or a new board to keep playing
    """
    if not board:
        return False
    who = winner(board)
    if who == "X":
        print(red("\n{} is the winner!\n".format(who)))
        return False
    elif who == "O":
        print(cyan("\n{} is the winner!\n".format(who)))
        return False
    elif full(board):
        print(green("\nStalemate.\n"))
        return False
    else:
        return board


def cpu_vs_cpu(strategy_x, strategy_o): # Module Engine
    """Game mode 0: run the game between two CPU opponents"""
    board = make_board()
    while True:
        show(board)
        board = cpu_turn(board, 'X', strategy_x)
        if not keep_playing(board):
            break
        show(board)
        board = cpu_turn(board, 'O', strategy_o)
        if not keep_playing(board):
            break
    show(board)


def cpu_vs_human(cpu_strategy): # Module Engine
    board = make_board()
    while True:
        show(board)
        board = cpu_turn(board, 'X', cpu_strategy)
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    show(board)


def human_vs_human(): # Module Engine
    board = make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    show(board)


def human_vs_cpu(cpu_strategy): # Module Engine
    board = make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        show(board)
        board = cpu_turn(board, 'O', cpu_strategy)
        if not keep_playing(board):
            break
    show(board)


def game(strategy_x, strategy_o): # Module Engine 
    global CPU_DELAY
    clear()
    print(green("GREETINGS PROFESSOR FALKEN\n"))
    sleep(CPU_DELAY)
    print(green("SHALL WE PLAY A GAME?\n"))
    sleep(CPU_DELAY * 2)
    orig_delay = CPU_DELAY
    clear()
    for _ in range(40):
        board = make_board()
        clear()
        while True:
            if CPU_DELAY > 0.025:
                CPU_DELAY *= 0.95
            home()
            show(board)
            board = cpu_turn(board, 'X', strategy_x, verbose=False)
            if not keep_playing(board):
                break
            home()
            show(board)
            board = cpu_turn(board, 'O', strategy_o, verbose=False)
            if not keep_playing(board):
                break
        clear()
        show(board)
        keep_playing(board)
        sleep(CPU_DELAY)
    CPU_DELAY = orig_delay
    sleep(CPU_DELAY)
    print(green("A STRANGE GAME.\n"))
    sleep(CPU_DELAY * 2)
    print(green("THE ONLY WINNING MOVE IS NOT TO PLAY.\n"))
    sleep(CPU_DELAY * 2)
    print(green("HOW ABOUT A NICE GAME OF CHESS?\n"))
    sleep(CPU_DELAY * 5)

# I think all of these functions are just utility functions.
def black(s):
    return "\x1b[1;30m{}\x1b[0m".format(s)


def red(s):
    return "\x1b[1;31m{}\x1b[0m".format(s)


def green(s):
    return "\x1b[1;32m{}\x1b[0m".format(s)


def yellow(s):
    return "\x1b[1;33m{}\x1b[0m".format(s)


def blue(s):
    return "\x1b[1;34m{}\x1b[0m".format(s)


def magenta(s):
    return "\x1b[1;35m{}\x1b[0m".format(s)


def cyan(s):
    return "\x1b[1;36m{}\x1b[0m".format(s)


def white(s):
    return "\x1b[1;37m{}\x1b[0m".format(s)


def color(s):
    if s == 'X':
        return red(s)
    elif s == 'O':
        return cyan(s)
    else:
        return white(s)


def home():
    """return cursor to home position (upper left corner)"""
    print(end="\x1b[H")


def clear():
    """clear the screen and return cursor to home position"""
    print(end="\x1b[H\x1b[J", flush=True)


if __name__ == '__main__':           # Module ttt.py 
    while True:
        logo()
        mode = player_select()
        if mode == 0:
            cpu_vs_cpu(strategy_oracle, strategy_oracle)
        elif mode == 1:
            human_vs_cpu(strategy_oracle)
        elif mode == 2:
            cpu_vs_human(strategy_oracle)
        elif mode == 3:
            human_vs_human()
        elif mode == 4:
            game(strategy_oracle, strategy_oracle)
        else:
            break
    print("Thanks for playing!")
