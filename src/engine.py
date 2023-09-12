from time import sleep

# Import Statements:
import ai
import interface
import util



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


def cpu_turn(board, letter, strategy, verbose=True): # Module Engine
    if letter == "X":
        color = util.red
    else:
        color = util.cyan
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


def open_cells(board): # module engine
    """ Returns a tuple of the unmarked cells in a Tic-Tac-Toe board """
    openings = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 'X' and board[row][col] != 'O':
                # convert (row,col) into a number
                openings.append(rowcol_to_pos(tuple([row, col])))
    return tuple(openings)


def first_open_cell(board): # module engine
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


def cpu_vs_cpu(strategy_x, strategy_o): # Module Engine
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


def cpu_vs_human(cpu_strategy): # Module Engine
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


def human_vs_human(): # Module Engine
    board = interface.make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    interface.show(board)


def human_vs_cpu(cpu_strategy): # Module Engine
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


def game(strategy_x, strategy_o): # Module Engine 
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
