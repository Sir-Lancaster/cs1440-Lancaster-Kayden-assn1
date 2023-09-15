from time import sleep

# Module Import Statements:
import ai
import interface
import util

CPU_DELAY = 0.75

def place(board, position, player):
    """
    Accepts: a game board (tuple), position (integer), and a player's identity ("X" or "O")
    Return a copy of the board with that player's mark put into the requested
    position, iff a player's mark isn't already present there.

    Otherwise, return False
    """
    if not 1 <= position <= 9:
        # player requested an out-of-bounds position
        return False

        # Ensures that the choses space is not occupied
    if board[position - 1] != 'X' and board[position - 1] != 'O':
        # construct a brand new board
        new = []
        for r in board:
            new.append(r)
        if new[position-1] == 'X' and new[position- 1] == 'O':
            return False
        else:
            new[position- 1] = player
        # Always maintain the board as a tuple to guarantee that it
        # can never be accidentally modified
        return tuple([new[0], new[1], new[2], new[3], new[4], new[5], new[6], new[7], new[8]])
    else:
        return False


def horizontal_winner(board):
    """
    Determines which player has won a game with a horizontal triple.
    Input: the game board.
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
    return (board[0] == board[1] == board[2] and board[2]) \
        or (board[3] == board[4] == board[5] and board[5]) \
        or (board[6] == board[7] == board[8] and board[8])


def vertical_winner(board): 
    """
    Determines which player has won a game with a vertical triple
    """
    return (board[0] == board[3] == board[6] and board[0]) \
        or (board[1] == board[4] == board[7] and board[1]) \
        or (board[2] == board[5] == board[8] and board[2])


def diagonal_winner(board): 
    """
    Determines which player has won a game with a diagonal triple
    """
    return (board[0] == board[4] == board[8] and board[8]) \
        or (board[6] == board[4] == board[2] and board[2])


def winner(board): 
    """
    Returns the winner of the game (if any), or False when there is no winner
    """
    return horizontal_winner(board) or vertical_winner(board) or diagonal_winner(board)
 
def human_turn(board, letter): 
    """
    Return False if the game is over,
           True to keep playing
    """
    while True:
        choice = interface.get_human_move(board, letter)
        if choice is False:
            return False
        new_board = place(board, choice, letter)
        if not new_board:
            if letter == 'X':
                print(util.red("You can't play at {}!".format(choice)))
            else:
                print(util.cyan("You can't play at {}!".format(choice)))
        else:
            return new_board


def cpu_turn(board, letter, strategy, verbose=True): 
    if letter == "X":
        color = util.red
    else:
        color = util.cyan
    if verbose:
        print(color("CPU {} is taking its turn...".format(letter)), end=' ', flush=True)
    sleep(CPU_DELAY)
    choice = strategy(board)
    if verbose:
        print(color("playing on {}\n".format(choice + 1)))
    return place(board, choice + 1, letter)






def open_cells(b):
    """ Returns a tuple of the unmarked cells in a Tic-Tac-Toe board """
    cs = []
    for p in b:
        if type(p) is int:
            cs.append(p)
    return tuple(cs)


def first_open_cell(board): 
    """ Return the ID of the first unmarked cell in a Tic-Tac-Toe board """
    cells = open_cells(board)
    if cells != []:
        return cells[0]
    else:
        return None


def full(board): 
    return open_cells(board) == ()


def keep_playing(board): 
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
        print(util.red("\n{} is the winner!\n".format(who)))
        return False
    elif who == "O":
        print(util.cyan("\n{} is the winner!\n".format(who)))
        return False
    elif full(board):
        print(util.green("\nStalemate.\n"))
        return False
    else:
        return board


def cpu_vs_cpu(strategy_x, strategy_o): 
    """Game mode 0: run the game between two CPU opponents"""
    board = interface.make_board()
    while True:
        interface.show(board)
        board = cpu_turn(board, 'X', strategy_x)
        if not keep_playing(board):
            break
        interface.show(board)
        board = cpu_turn(board, 'O', strategy_o)
        if not keep_playing(board):
            break
    interface.show(board)


def cpu_vs_human(cpu_strategy):
    board = interface.make_board()
    while True:
        interface.show(board)
        board = cpu_turn(board, 'X', cpu_strategy)
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    interface.show(board)


def human_vs_human(): 
    board = interface.make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    interface.show(board)


def human_vs_cpu(cpu_strategy):
    board = interface.make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        interface.show(board)
        board = cpu_turn(board, 'O', cpu_strategy)
        if not keep_playing(board):
            break
    interface.show(board)


def game(strategy_x, strategy_o):  
    global CPU_DELAY
    util.clear()
    print(util.green("GREETINGS PROFESSOR FALKEN\n"))
    sleep(CPU_DELAY)
    print(util.green("SHALL WE PLAY A GAME?\n"))
    sleep(CPU_DELAY * 2)
    orig_delay = CPU_DELAY
    util.clear()
    for _ in range(40):
        board = interface.make_board()
        util.clear()
        while True:
            if CPU_DELAY > 0.025:
                CPU_DELAY *= 0.95
            util.home()
            interface.show(board)
            board = cpu_turn(board, 'X', strategy_x, verbose=False)
            if not keep_playing(board):
                break
            util.home()
            interface.show(board)
            board = cpu_turn(board, 'O', strategy_o, verbose=False)
            if not keep_playing(board):
                break
        util.clear()
        interface.show(board)
        keep_playing(board)
        sleep(CPU_DELAY)
    CPU_DELAY = orig_delay
    sleep(CPU_DELAY)
    print(util.green("A STRANGE GAME.\n"))
    sleep(CPU_DELAY * 2)
    print(util.green("THE ONLY WINNING MOVE IS NOT TO PLAY.\n"))
    sleep(CPU_DELAY * 2)
    print(util.green("HOW ABOUT A NICE GAME OF CHESS?\n"))
    sleep(CPU_DELAY * 5)
