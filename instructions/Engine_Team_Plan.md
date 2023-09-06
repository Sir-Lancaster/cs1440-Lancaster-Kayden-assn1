# Software Development Plan - Game Engine & UI Team

## Phase 0: Requirements Analysis
*(20% of your effort)*

### Re-write the instructions in your own words

The project calls for a prototype of an interactive Tic-Tac-Toe game that will be played in the console.  This means text input and output, and ASCII art instead of real pictures.  Lots of `print` and `input`.  There will be an AI opponent, meaning that both single- and two-player modes will be created.  There will be a zero-player mode that will let the human player watch the AI fight itself.  That will either be very interesting, or very boring.

The game is required to incorporate colors and to be "colorful and attractive".  We are very limited in a text console with what we can do about this, but we'll do our best.  Simplicity will be key.


### Explain the problem this program aims to solve

The game needs to support anywhere from 0 to 2 players; in single-player mode the Human player has the option of taking the side of either 'X' or 'O'.

The basic game loop was described like this in the requirements doc:

0.  X plays
1.  Check for end condition
2.  O plays
3.  Check for end condition
4.  Repeat

This much is very straightforward.  However, the requirement is that each of the players can be CPU- **or** human-controlled.  This means there are four possibilities for how the game can be played:

0.  CPU vs. CPU
1.  Human vs. CPU
2.  CPU vs. Human
3.  Human vs. Human

We *might* be able to do this with a single game loop function, but it could take as many as four different functions.

We won't have the final version of the CPU player until near the end of the project; the AI team will have their hands full designing an optimal player.  In the meanwhile we can ask them to provide a "dummy" AI (in both senses of the word) that we can plug in for testing purposes.  It would be nice if we can find a way to easily replace the AI while testing.  Perhaps we could (in a future version) offer different levels of difficulty by providing AI's with differing degrees of "intelligence".  A game like this just *screams* for a call-out to the 80's classic *WarGames*.

The game also needs to keep track of which squares have been played by which player, and to detect when a game has won.  The requirements state that the Tic-Tac-Toe game board is a 3x3 grid.  It seems that a 2D array will be the most natural way to keep the game state.  It shouldn't be too hard to write code that can search the array for 3-in-a-row of the same symbol.  We'll also need to think of a way for the user to indicate which square to play.


#### Describe what a *good* solution looks like

*   Playable game - no unexpected crashes or glitches
*   Input is handled smartly; don't frustrate the user by being too picky with input
*   Output is clean and spare; don't overwhelm the player with too much text, nor crowd the screen with too much information


#### List what you already know how to do

*   Get input from the user
    *   How to be reasonably forgiving with input; for example, accepting case-insensitive inputs
    *   Ask the user which square to play
        *   one idea is to name the squares by cardinal direction: NW, N, NE, E, SE, etc.
        *   another popular idea is to just number them from left to right, top to bottom, starting at 1
*   Write a simple, single-player game loop


#### Point out any challenges that you can foresee

*   Nobody on the team knows how to make colors work on a text terminal
*   Stepping up from a simple single-player game loop to one that can accommodate all of the different combinations of players
*   Detecting when a player has won, or when the game is drawn


### List all of the data that is used by the program, making note of where it comes from

#### Input
*   All of the data will come from the user via the `input` function.
    *   There will be at least a Main Menu that lets the user choose the game mode (0, 1, or 2 players)
    *   The user will be able to enter <kbd>q</kbd> or <kbd>Q</kbd> to quit
    *   Human players can input the name of a square to place their mark
*   The game will need to validate all user input so that crashes are avoided

#### Output

*   All output will be sent to the screen with the `print` function
*   Some output will be **colored**
    *   Preliminary research says that this is done in the terminal with something called "escape sequences"
*   The logo for the game will be a big, triple-quoted string that is printed once before the main menu is displayed
*   The game board will likely be the most complex thing the program will output
    *   It will have nine spots that need to be filled in with dynamic content
    *   The spacing between symbols and the "walls" of the squares must always be maintained so the board is easy to read
*   Messages that explain what is going on should be brief, clear and useful
    *   Extraneous output will be curtailed so that we don't overwhelm the player.


### Algorithms and formulae to be used

*   An algorithm that reads the board state and detects the winner (or a draw)
    *   Perhaps this should be broken up into **3** different cases:
        *   A winner along a horizontal line
        *   A winner along a vertical line
        *   A winner along a diagonal line
    *   Each of these by itself feels like a simple function to write
    *   These are easily combined with `or` logic:
        *   `return horizontal() or vertical() or diagonal()`
*   A game loop algorithm that supports switching out CPU and human players
*   ~~An algorithm that applies the AI team's strategy function to the game board and picks the next best move~~ never mind, this is what the AI team is doing
*   An algorithm that updates the game board by placing a new mark
*   An algorithm that checks whether a player's move is legal (i.e. don't allow a player to put their mark on a square that already has a mark)


## Phase 1: Design
*(30% of your effort)*

Functionality will be broken up into three big categories:

1.  Miscellaneous Utilities
2.  Game Engine
3.  User Interface

As an aside, everybody calls us the "UI" team.  But as you can see here, the user interface is only a small part of what we do.


### 1. Miscellaneous Utilities

#### `make_board` - return a new game board

A game board is a 3x3 grid of squares.  We like the guarantees that immutability gives, and will make this a 3-tuple of 3-tuples instead of a list of lists.  The game board is initialized with the numbers 1-9.  These numbers are replaced with X's and O's as the game progresses.  This is how the program knows if a square has already been played.  The numbers also signify to the user where to place their mark.  A pair of simple functions will translate between the integers 1-9 and the X,Y coordinates of the squares.

```python
def make_board():
    """return a fresh game board"""
    return ((1, 2, 3),
            (4, 5, 6)
            (7, 8, 9))
```


#### `pos_to_rowcol` - convert integer 1-9 to X,Y coords

The formula for this conversion is simple.  The trick is remembering that the user will be presented the squares starting at 1, but Python tuples are indexed from 0.

```python
def pos_to_rowcol(position):
    subtract 1 from position
    the row is the quotient of INTEGER division of position by 3
    the column is the remainder of INTEGER division of position by 3
    return (row, column)
```


#### def `rowcol_to_pos` - convert X,Y coords to integer 1-9

The inverse of the above function.  As before, the result is biased by 1 to account for the underlying tuple being indexed from 0

```python
def rowcol_to_pos(row, column):
    return (row * 3) + column + 1
```


#### `place` - return a new board with letter at position (if possible)

This function will return a new game board when the human player makes a legal move, or returns `False` if that move was illegal.  The UI function `get_human_move()` will inspect the return value when it decides whether to proceed or prompt the user to try again.

```
def place(board, position, letter):
    """
    Accepts: a game board (tuple), position (integer), and a player's identity ("X" or "O")
    Return a copy of the board with that player's mark put into the requested
    position, iff a player's mark isn't already present there.

    Otherwise, return False
    """
    row, column = pos_to_rowcol(position)
    bounds-check: row and column are both between 0 and 2
    if board[row][column] is not an integer, return False because the user tried to place their letter on a square that is taken
    else:
        # make the board into a list of lists (LoL, get it?)
        LoL = []
        for row in board:
            LoL.append(list(row))
        LoL[row][column] = letter
        # convert LoL back into a tuple
        return tuple([ tuple(LoL[0]), tuple(LoL[1]), tuple(LoL[2])])
```


#### `winner`

We spent a lot of time designing the functions that decide when the game is over.  We made checking for the winning states a lot more complex than it needed to be!  But we ultimately settled on breaking the task down into 3 steps, each of which isn't too bad on its own.

These three helper functions return either the letter of the winning player, or `False`.  This function combines these results using the boolean `or` operator.

Usually, we don't put finished code into the plan document.  However, in this case the finished code is so simple that it is basically pseudocode!

```python
def winner(board):
    return horizontal_winner(board) or vertical_winner(board) or diagonal_winner(board)
```


#### `horizontal_winner`

First, check whether the three squares in the top row are all the same.  This is ONLY true when the same player has played their mark there.  If so, return the letter in the upper-right corner (it doesn't matter which of the 3 we return).

Once we figured this out, the other two rows were super easy to check.  Just repeat the process for the 2nd row, then the 3rd.

Using this same technique, checking for vertical and diagonal winners is a cinch.

```python
def horizontal_winner(board):
    """
    Determines which a player has won a game with a horizontal triple.
    Input: a 2D game board.
    Return: 'X' or 'O' when there is a winner, or False when no player has 3 in
    a horizontal row
    """
    if all squares in 1st row are equal:
        return upper-right square
    elif all squares in 2nd row are equal:
        return middle-right square
    elif all squares in 3rd row are equal:
        return bottom-right square
    else:
        return False
```

While testing this function we discovered a shorter way to say the same thing that doesn't use `if` or `elif`.  It relies on the fact that Python's `and` and `or` operators return values besides just `True` and `False`.  We felt that it was more readable, and hope it is not too clever.  See the final version in the code.


#### `vertical_winner`

Same as above, but check column-wise instead of row-wise:

```python
def vertical_winner(board):
    """
    Determines which a player has won a game with a vertical triple
    """
    if all squares in 1st column are equal:
        return top-left square
    elif all squares in 2nd column are equal:
        return top-middle square
    elif all squares in 3rd column are equal:
        return top-right square
    else:
        return False
```


#### `diagonal_winner`

Same as above, checking the two diagonals:

```python
def diagonal_winner(board):
    """
    Determines which a player has won a game with a diagonal triple
    """
    if all squares in top-left to bottom-right diagonal are equal:
        return middle square
    elif all squares in bottom-left to top-right diagonal are equal:
        return middle square
    else:
        return False
```


#### `open_cells` - returns a tuple of the unmarked squares in a Tic-Tac-Toe board

The numbers in this tuple correspond to the valid moves the player may take

```python
def open_cells(board):
openings = []
for each row:
    for each column:
        if board[row][column] is an integer:
            append board[row][column] to openings
return tuple(openings)
```


#### `full` - predicate: test whether board is full or not

When the board is full, the game is over.  We check this condition AFTER testing for a winner; if the board is full and nobody has 3-in-a-row, the game is a draw.

This function is very simple: just return True if `open_cells()` returns an empty tuple:

```python
def full(board):
    if open_cells() == ():
        return True
    else:
        return False
```

Four lines of code to return `True` or `False` seemed like too much.  We thought about it and came up with this formulation that just returns the result of the `==` test:

```python
def full(board):
    return open_cells() == ()
```

That's much cleaner!



### 2. Game Engine

#### `keep_playing` - predicate: test whether the game should continue or is finished

Accepts a board or False as input
       board: take another turn
       False: the user has requested to quit the game
Return False if the game is over for any reason (quitting, win, lose or draw),
       or a new board to keep playing

```python
def keep_playing(board):
    if board is False, return False

    # Check the board for a winner using winner(board)
    # This is why winner() returns a player's identity instead of True or False
    w = winner(board)
    if w is 'X', print a message congratulating player X
    if w is 'O', print a message congratulating player O

    # if the board is full, declare a draw
    if full(board): print("It's a draw game!")

    # If all of these tests fail, the game is still ongoing.
    # Return the game board to keep playing
    return board
```



#### `human_turn` - let a human player take their turn at the game

This function uses `get_human_move()` to ask the user where they want to play.  That takes care of validating that their input is numeric and in the range 1..9.  If the user tells `get_human_move()` that they want to quit, we will see a False value, which we will return to our caller to signal the end of the game.

Next, it uses `place()` to attempt to put their mark in that square.  If that works, we get a new game board back.  When `place()` returns False, that means the user picked a square that is already taken.  In this case, the user is asked to pick a different square.  There will be a loop of some kind (probably a `while` loop), that repeats this question until the user picks an open square.

Overall, this function returns False if the game is over (because the player wants to quit), and True to keep playing.

```python
def human_turn(board, letter):
    forever:
        square = call get_human_move()
        if square is False, return False (the player wants to quit)
        make a new_board by placing "square" on the board with place()
        if the new_board is False:
            print("You can't put your mark on square", square)
        else:
            return new_board
```


#### `cpu_turn` call upon an AI engine to pick a square to play

This function is pretty simple - it exists to print out some messages for the Human player's benefit, so they can follow what's going on.  In the middle of this, it will call out to the AI strategy function to do the smart stuff.

This function will use Python's `sleep()` function to slow things down a bit for the human player's benefit.  It will take some trial-and-error to decide how long to delay the game.

This function will need to have access to

0.  The current game board
1.  The letter this CPU player marks the board with
2.  An AI strategy function

Because function names are just like variables in Python, `cpu_turn()` can accept an AI strategy function as a parameter and call it when needed, like a plug-in.  This will let us test out different AI strategies.  This isn't called for in the requirements, but maybe in version 2.0 many AI strategy functions could be created to provide various levels of difficulty.  In this project we will use this feature to test our code with a "stupid" AI while the other team works on the "smart" one.

I suggested this to the AI team early in the project over a game of Foosball (those guys think they are all so good at that game, but I always hold back so they don't get upset; they're a bunch of sore losers).  This is functional programming 101, but they acted like it was Voodoo.  I was under the impression that AI people knew about functional programming.  I guess they didn't go to the same school as me.  I passed functions to functions all the time in Intelligent Systems (CS 5600) at USU.  Heck, with my background *I* should be making the AI!

In this example, `strategy` is the AI function:

```python
def cpu_turn(board, letter, strategy):
    print("CPU player", letter, "is taking their turn...")
    sleep()
    choice = strategy(board)
    new_board = place(board, choice, letter)
    return new_board
```


#### Game loops

There are 4 ways this game can be played:

0.  CPU X vs. CPU O
1.  Human X vs. CPU O
2.  CPU X vs. Human O
3.  Human X vs. Human O

We had originally considered writing one big game loop that used `if`/`elif` to choose which one of `cpu_turn` and `human_turn` to call at each juncture.  But it quickly became clear that design wasn't going to be easy to write (or read!).  The problem is that each branch of the `if`/`elif` was too long and complicated.

We now believe that moving the `if`/`elif` out of this function is the right approach.  This makes us split the game loop up into *four* separate functions.  Each one is simple and clean, and the `if`/`elif` decision tree is also shorter and easier to understand.

Each of the functions that supports a CPU player needs a parameter that contains the strategy function for that player.  This enables us to pit a "stupid" AI against a "smart" AI.  That will be fun to watch when the AI team finishes their work.

Each function resembles the others.  This is what they will look like:

##### `cpu_vs_cpu`

```python
def cpu_vs_cpu(x, o):
    make a fresh board with make_board()
    forever:
        show the board
        Take CPU x's turn
        Check to see if the game is over; break the loop if X has won or drawn

        show the board
        Take CPU O's turn
        Check to see if the game is over; break the loop if O has won or drawn
    Show the board one last time
```

##### `human_vs_cpu`

```python
def human_vs_cpu(cpu_strategy):
    make a fresh board with make_board()
    forever:
        Take Human x's turn (this shows the board)
        Check to see if the game is over; break the loop if X has won or drawn

        show the board
        Take CPU O's turn
        Check to see if the game is over; break the loop if O has won or drawn
    Show the board one last time
```

##### `cpu_vs_human`

```python
def cpu_vs_human(cpu_strategy):
    make a fresh board with make_board()
    forever:
        show the board
        Take CPU x's turn
        Check to see if the game is over; break the loop if X has won or drawn

        Take Human O's turn (this shows the board)
        Check to see if the game is over; break the loop if O has won or drawn
    Show the board one last time
```

##### `human_vs_human`

```python
def human_vs_human():
    make a fresh board with make_board()
    forever:
        Take Human x's turn (this shows the board)
        Check to see if the game is over; break the loop if X has won or drawn

        Take Human O's turn (this shows the board)
        Check to see if the game is over; break the loop if O has won or drawn
    Show the board one last time
```


##### Easter Egg

We couldn't resist hiding a special game mode that calls back to a classic Hacker movie.  We'll rename this function in the final version to make it less obvious in the source code.  The Easter Egg is a hidden game loop that operates like CPU vs. CPU, except several games are played and each turn accelerates the speed, going faster, and faster until the games fly by in a blur.

Before and after the games are played, the program prints out some dialog from the movie.  We hope it's appreciated by more than boomers.

Fans of the movie "WarGames" will know what to type at the main menu to enter the cutscene.  If you aren't familiar with the movie, you can "use the source".

```python
def wargames(strategy_x, strategy_o):
    print introductory dialog from the movie

    for 50 or 60 games
        make a fresh board with make_board()
        forever:
            show the board
            Take CPU x's turn
            Reduce the sleep delay by a fraction
            Check to see if the game is over; break the loop if X has won or drawn

            show the board
            Take CPU O's turn
            Reduce the sleep delay by a fraction
            Check to see if the game is over; break the loop if O has won or drawn
        Show the board one last time

    print the computer's dialog when it comes to the conclusion that TicTacToe is pointless
    Pause a beat to let it sink in, then return to the main menu
```


### 3. User Interface

#### Colored text with escape sequences

The first challenge we tackled is to learn how to print colored text on the console.  At first it seemed very complicated, but it was actually quite simple.  It is accomplished by printing special strings called "escape sequences".  They are called this because the first thing in the sequence is actually the <kbd>Escape</kbd> character.  The <kbd>Escape</kbd> key doesn't output anything when you press it.  There is another way to type it that is similar to the way we write tabs and newlines in source code.  It looks like this: `\x1b`, which means "output the byte denoted by the hexadecimal number 1b", which equates to the number 27.

After the "Escape" comes an open square bracket `[`, then some numbers separated by semi-colons `;`, and finally a lower-case letter `m`.  All text printed after this sequence is shown in that color until the "reset" sequence is encountered.  There are a lot of numbers that could go in the middle, but these ones seem to be the most useful:

*   `0` reset the color; make text appear normal again
*   `1` make the text show up brighter, or in a bold font
*   `30` black
*   `31` red
*   `32` green
*   `33` yellow
*   `34` blue
*   `35` magenta
*   `36` cyan
*   `37` white

**Examples:**

```python
print("\x1b[1;31mThis text is bright RED\x1b[0m")

print("\x1b[1;33mNow it is YELLOW")

print("these words are still YELLOW, too\x1b[0m and now we're back to normal")
```

**Sources:**

*   [Wikipedia: ANSI color escapes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)
*   [ANSI escape sequence documentation](https://invisible-island.net/xterm/ctlseqs/ctlseqs.pdf)

For each color needed by the program we can define functions that let us choose the color of the text by name instead of needing to memorize which number between 30-37 corresponds to which color (I feel like there is some logical explanation for those numbers, but I'm not seeing it).

```python
def blue(string):
    return "\x1b[1;34m" + string + "\x1b[0m"
```

Originally, the team considered making these functions `print` a colored string.  But we now feel that it is better to just return a string.


#### `color` - automatically color X's and O's

We want all X's to be red, and O's to be green.  The above function taught us that choosing the color of each symbol with `if` statements will be too tedious.  So we designed a helper function to make that decision for us:

```python
def color(string):
    if string startswith 'X':
        return red(string)
    elseif string startswith 'O':
        return green(string)
    else
        return yellow(string)
```

This will surely have use elsewhere.


#### `clear` - clear the screen and return cursor to the home position

While digging through ANSI escape sequence documentation (linked above), we discovered that printing the string `"\x1b[H\x1b[J"` makes the terminal clear itself.  This seemed useful, so we put it into a function for convenience.

The `\x1b` part at the beginning and middle of that string represents the **Escape** key.  The portion including the open square bracket, `\x1b[`, is a code called "Control Sequence Introducer".  This is why they are called "escape sequences" - they literally start with Escape!

To make sure that the screen is cleared instantly, we pass `flush=True` to `print()`.  We also didn't want to output an extra newline as a side effect each time the screen is cleared.  The first version of this function suppressed the newline with `end=''`.  Later, we learned by accident that `print()` is perfectly happy when `end='...'` is the *only* text to be printed.  So, instead of giving `print()` three parameters, we only need two.


#### `home` - return cursor to the home position

Further reading taught us that the "clear screen" command is actually two separate escape sequences:

*   `\x1b[H` - move cursor to position 1, 1
*   `\x1b[J` - clear the screen from the cursor's position to the bottom

As we worked on an unspecified undocumented feature, we wanted to move the cursor without also erasing the entire screen (it reduces how much the screen flickers).  So we split this command out into its own function.


#### `logo` - Display the game's title

Ditto for the `logo()` function - our first idea was to just print it out, along with the hard-coded escape sequences.  Now we think that this function should use the named color functions and just return a string.  Something along these lines:

```python
def logo()
    """returns a big, triple-quoted string literal that is the game's ASCII-art logo"""
    return """\
 _______ _   _______      _______
|__   __(_) |__   __|    |__   __|
   | |   _  ___| | __ _  ___| | ___   ___
   | |  | |/ __| |/ _` |/ __| |/ _ \ / _ \
   | |  | | (__| | (_| | (__| | (_) |  __/
   |_|  |_|\___|_|\__,_|\___|_|\___/ \___|
"""
```

#### `show` - Display the game board as a neat, colorful grid.

We tried a few different versions of this function with varying arrangements of nested loops.  This led to complications with the vertical line between squares also appearing to the right of the game.  Ultimately, we arrived at a version that just accesses each item in the grid individually.  I think they call this "unrolling the loop" in the video game biz.

```python
def show(board):
    print(
    color(board[0][0]) | color(board[0][1]) | color(board[0][2])
    ---+---+---
    color(board[1][0]) | color(board[1][1]) | color(board[1][2])
    ---+---+---
    color(board[2][0]) | color(board[2][1]) | color(board[2][2])
    )
```


#### `get_human_move` - prompt the player for a move and validate

Ask a human which move to take, or whether they want to quit.  Perform rudimentary input validation, repeating the prompt until a valid input is given:

*   Integers must be in the range of [1..9] (whether it represents a legal move
    is to be handled by the caller)
*   Strings beginning with 'Q' or 'q' quit the game

Return an integer [1..9] to indicate the move to take, or False to quit the game

```
def get_human_move(board, letter):
    forever:
        show the game board
        prompt user for number [1..9], or Q to quit
        If the input (lowercase) starts with q, return False
        If the input is not a digit, "I don't understand your input, try again!"
            continue
        If the input is a digit, check that it is >0 and <10 or else print
            "Numbers must be between 1 and 9, try again!\n"
        If the input is a digit in the correct range, convert it to an integer and return
```

Things to keep in mind:

1.  The user's input is a **string**
2.  It is safe to convert it with `int()` when the input is validated to be made of digits
3.  While this function does a little bit of validation, it is another function's job to make sure this number hasn't already been played


#### `player_select` - ask for # of players, or quit

This function handles asking the player what game to play, validating their input, and exiting.

The menu is repeated until the user provides a valid response.

```python
def player_select():
    forever:
        Ask user for a game "mode", which is a number of players or "q" to quit
        mode 0:
            CPU_VS_CPU mode
        mode 1:
            single player mode
        mode 2:
            two human player mode
        mode starts with the letter "Q" (upper or lowercase)
            exit
        otherwise print the  message "That was an invalid input"
```


#### Main menu

This may or may not be a function unto itself.  But the first thing the user will see is the game logo, followed by this menu that asks for a number of players.

```python
while True:
    print the logo()
    player_select()
```

This structure ensures that the logo is printed only at the start of the program, or after a game has ended.  We don't want to spam the user with that big block of text every time they make a typo!



## Phase 2: Implementation
*(15% of your effort)*

We couldn't decide whether to call them "squares" or "cells".  But we heard that the AI team was using the word "cells", so we followed suit to maintain compatibility.

Almost all of our functions were easily translated from pseudocode into Python.

We decided that a delay of 3/4th of a second for the CPU player to take its turn was the best for making the game flow at a good pace.

The one that gave us the most trouble was `WarGames()`.  This was because we stored the CPU player's delay in a global constant, but we needed to change it in order to accelerate the games.  This reminded us why global variables are a bad idea!  We had to be very careful to restore the original value of this "constant", otherwise subsequent games with a CPU player flew by too fast!

It is possible to re-write the affected functions to avoid changing a global; simply make the delay into a parameter of `cpu_turn()`.  But by the time we discovered this, it was just easier to leave our code as it was.  It *does* work, after all.  I suppose this indicates that we didn't plan out our Easter Egg too well.  The lesson to draw from this is to really think about how the program will run while it's still pseudocode!


## Phase 3: Testing & Debugging
*(30% of your effort)*

In the beginning, before the AI team provided a "dummy" game engine for testing, we were able to test the game engine in the 2-player mode.  This enabled us to ensure that input validation and end-state detection worked.

### Main Menu Input Validation

Valid menu options are [0-3], and strings beginning with `q` or `Q` quit the program.

The game logo is shown *once* when the game begins.

*   Enter `-1`
    *   The message `Invalid selection!` is shown, and the menu is repeated.
    *   The logo is not redisplayed
*   Enter `4`
    *   The message `Invalid selection!` is shown, and the menu is repeated.
    *   The logo is not redisplayed
*   Enter `three`
    *   The message `Invalid selection!` is shown, and the menu is repeated.
    *   The logo is not redisplayed
*   Enter `quincy quail quietly stacked quarters for the queen`
    *   This is interpreted as a *quit* command, and the program exits


### Game Input Validation

Valid plays are [0-9], and strings beginning with `q` or `Q` quit the game.

*   Restart the program and enter `3` to begin a 2-player game
    *   A fresh Tic-Tac-Toe game board is displayed and player 'X' is asked for their move
*   X attempts to play in square 10
    *   The message `Numbers must be between 1 and 9, try again!` is shown, and the prompt repeated
*   X attempts to play in square 0
    *   The message `Numbers must be between 1 and 9, try again!` is shown, and the prompt repeated
*   X attempts to play in square `seven`
    *   The message `I don't understand 'seven', try again!` is shown, and the prompt repeated
*   X plays in square 1
*   O attempts to play in square 1
    *   The message `You can't play at 1!` is shown, and the prompt repeated
*   O enters `Quentin's duck went "Quack, Quack, Quack!"`
    *   This is interpreted as a *quit* command, and the main menu reappears

With these testing steps we found off-by-one errors in `pos_to_rowcol()` and `rowcol_to_pos()`.  These were remedied by subtracting one from the input position in `pos_to_rowcol()`, and adding one to the value returned by `rowcol_to_pos()`.


### End-State Detection

*   Horizontal win
    *   Enter a 2-player game
    *   Enter these numbers in this order to force X to win in the middle row:
        *   4, 1, 5, 2, 6
*   Vertical win
    *   Enter a 2-player game
    *   Enter these numbers in this order to force O to win in the right column:
        *   2, 3, 1, 6, 4, 9
*   Diagonal win
    *   Enter a 2-player game
    *   Enter these numbers in this order to force X to win in the 1,5,9 diagonal:
        *   1, 3, 5, 7, 9
*   Draw game (cat)
    *   Enter a 2-player game
    *   Enter these numbers in this order to force a draw:
        *   5, 2, 7, 3, 1, 9, 6, 4, 8

Win detection was originally one long function named `winner()` that checked all of the 8 different ways a game could be won.  But we kept making small typographical mistakes that resulted in the program failing to detect when the game was over.

This convoluted logic was split into the three helper functions `horizontal_winner()`, `vertical_winner()` and `diagonal_winner()`.  Somehow, that simple change cleared everything up!

`winner()` is now a trivial and straightforward function that reads like plain English:

```python
horizontal_winner(board) or vertical_winner(board) or diagonal_winner(board)
```

How do you mess that up?


## Phase 4: Deployment
*(5% of your effort)*

Done and done


## Phase 5: Maintenance

### What parts of your program are sloppily written and hard to understand?

The Easter Egg code

### Are there parts of your program which you aren't quite sure how/why they work?

The individual functions are straightforward enough.  But we sometimes get lost in how they all work together.

### If a bug is reported in a few months, how long would it take you to find the cause?

Not too long... each function has a clear purpose.  It should be a simple matter to trace the cause of the bug back to one of those functions.  Once it's narrowed down that far, there aren't too many lines of code for it to be hiding in.

### Will your documentation make sense to anybody besides yourself?

Yes.  We spell checked it.

### Will your documentation make sense to yourself in six month's time?

This documentation is the only way we are able to follow the flow of the program.  We've been relying on it already.  It will be our lifeline as we maintain this program for the coming years.

### How easy will it be to add a new feature to this program in a year?

It depends on the feature.

*   Changing colors, messages, etc. will be easy.
*   Adding a new AI personality will be *very* easy.
*   Creating entirely new game modes (i.e. network play) will be hard; this would require a big rewrite.


### Will your program continue to work after upgrading your computer's hardware/ operating system/ Python version?

We avoided platform-specific code.  We have no reason to believe this program will behave any differently in other environments.

We intentionally avoided newfangled features of Python, as well as things that we can reasonably expect to be deprecating in upcoming versions.  This Tic-Tac-Toe game should keep on ticking!
