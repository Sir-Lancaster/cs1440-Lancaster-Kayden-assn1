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
