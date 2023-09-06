# CS 1440 Assignment 1: Tic-Tac-Toe - Project Requirements

*This is the requirements document that the original teams followed.  Read this with their SDPs to understand what they set out to accomplish.*

*   Create an interactive Tic-Tac-Toe game that supports 0, 1 or 2 players.
    *   In 0 player mode, the human observer watches two CPU-controlled players battle it out.
        *   The CPU-powered opponent should be equally adept at playing 'X' and 'O'.
    *   Two single-player modes will be offered, allowing a human player to play as 'X' or 'O'.
*   In two player mode, two humans compete against each other (or, one player can match wits with themself?)
*   Game modes featuring a CPU player use a machine-learning (ML) model to choose the best move.
    *   This provides the greatest challenge for players, and maximizes the buzzword potential for the marketing team.
    *   If our research is correct, optimal CPU opponents should always play to a *draw*.


## User Interface

### Interface Design Principles

*   The program should be colorful and attractive
    *   Colors should be used tastefully, consistently and sparingly
*   Messages and prompts should be clear and concise
*   The game board should be easy to read at a glance
*   The interface should never allow the user to become "stuck"
    *   There should always be a way to exit back to the main menu
    *   The main menu allows the user to quit the program


### Main Menu

*   Before the main menu first appears the program's logo is displayed.
*   The player is given choices of game modes, along with an option to quit the game <kbd>Q</kbd>.
    *   Actually, the game exits when **anything** beginning with either <kbd>Q</kbd> or <kbd>q</kbd> is entered (nothing is more frustrating than to be sent back into a menu when you type `"quit"` - the game should know what I meant!)
    *   Otherwise, an error message is shown and the menu is repeated when any other input is given, including spaces and when the user just hits <kbd>Enter</kbd> by itself.
    *   Do not re-display the logo when the menu is repeated
*   Each game mode is identified by a single character; these could be either a letter or a number.


### Logo

*   The title of the game, **Tic-Tac-Toe** should be displayed in a large ASCII art font before the menu is shown.
    *   It should be easy to read and colorful; it is the identity of the game!
    *   Incorporate the DuckieCorp brand name unobtrusively.
*   When a game ends a message is displayed indicating the disposition (which player won, or whether it was a drawn game).
    *   The logo is printed again and control is returned to the main menu.


### Game board

*   Display a 3x3 grid.
    *   In each square appears one of an 'X', 'O', or identifying number.
*   When it is a human player's turn a prompt is given asking which square they want to place their mark into.
    *   The only valid inputs are the digits 1-9, and of those only numbers corresponding to open squares are accepted.
    *   <kbd>Q</kbd> quits the game, returning the player to the main menu.
    *   As with the main menu, the user may actually enter **any** string starting with <kbd>Q</kbd> or <kbd>q</kbd> to quit.
*   When the player inputs the number of a square that has already been played, an error message is shown and the board and prompt are repeated.
    *   If the user gives other invalid inputs (including spaces and just hitting <kbd>Enter</kbd> by itself), an error message is shown and the board and prompt are repeated.


### Colors

*   Make the game attractive by adding splash of color!
    *   But don't over-do it - use a consistent color palette throughout the game:
        *   X marks and messages related to the 'X' player are printed in **red**
        *   O marks and messages related to the 'O' player are printed in **green**
        *   A different, neutral color is used to print the square ID's in the game board
        *   One more contrasting color may be used for emphasis


## Gameplay

*   Tic-Tac-Toe is a game between two players, X and O, who take turns marking a 3x3 game grid.
    *   The X player always takes the first turn.
    *   A player wins when they mark 3 squares in a straight line vertically, horizontally or diagonally.
*   Good strategy dictates that players strive to block their opponent's lines while setting up their own.
    *   Optimal strategy played by both sides always leads to a drawn game.
    *   A drawn game occurs when no lines are complete and no free squares remain (i.e. the board is full).


### Game Loop

Turns proceed as follows:

0.  X plays
1.  Check for end condition
2.  O plays
3.  Check for end condition
4.  Repeat

*   In this program, the two sides can be under the control of any combination of human or CPU.
    *   Thorough testing is required to ensure the game accurately detects the end conditions and credits victory to the correct player.
*   A brief, artificial delay should be introduced when the CPU player takes its turn to slow down the pace of the game.
    *   Otherwise, the CPU's turn will go by in an instant, breaking the pace of the game and making it harder for the human to keep up with the action (especially in the 0-player game).
    *   A message like "the CPU is thinking..." may be shown during the delay.


## Artificial Intelligence

*   The heart of the CPU-controlled opponent is an AI that utilizes Machine Learning (ML) like ChatGPT or LLaMa2.
    *   The goal is to make the game as challenging as mechanically possible.
    *   This game is targeted to the professional Tic-Tac-Toe community, who expects nothing less than a strong challenge.
    *   Since the game requires that the AI plays both as X and O, it should be equally adept at each side.
*   Our client says that we can use whatever means are necessary to create the AI player.
    *   This AI stuff isn't in their area of expertise; they just know that it's an important buzzword this year.
    *   The other important requirement they set for us is that this game "should be at least a bit faster than those chess games".
*   After the AI is written, it should be thoroughly tested to ensure that it cannot lose.
    *   The AI must win or draw every game it plays.
