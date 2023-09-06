# Software Development Plan - AI Team

## Phase 0: Requirements Analysis
*(20% of your effort)*

### Re-write the instructions in your own words

Our team has been asked to design and implement a machine-learning (ML) based
Tic-Tac-Toe engine that plays an optimal game.  Tic-Tac-Toe is a solved game,
meaning that the outcomes of all possible games have been computed in advance.
It is known that two players who make optimal moves will always draw.  This
means that our AI should never lose; the worst it can do is tie.

In our game the AI will be capable of playing against itself.  This suggests a
good testing strategy - we can simulate many games and check that they always
end in draws.


### Explain the problem this program aims to solve

Our client wants a Python solution that makes use of ML.  Fortunately, Python
has some very good choices of ML frameworks for us to select from.

We very quickly rejected the customer's suggested ML approach as too heavy
weight.

*   On our development computers the PyTorch library takes 1.8GB of disk space.
    There is no way that we are going to ship a Tic-Tac-Toe game that weighs as
    much as an XBox game.
    *   It takes 1.07 seconds to load PyTorch at the beginning of the program.
        We believed that our AI should be able to play hundreds of games in
        that amount of time
    *   Do they seriously want to require their users to own a top-of-the-line
        graphics card to play a game that doesn't have real graphics?
*   NumPy weighs in at 35MB.  This seems like spare change after considering
    PyTorch, but is still **way** to much code for a simple game like
    Tic-Tac-Toe.
    *   For comparison, the original version of DOOM from 1993 used about 12MB
        of disk space, and it had *graphics*

Our team came to the conclusion that a simple **Look Up Table** (LUT) is all
that is needed.  Randall Munroe, author of XKCD, created a LUT for one of his
[comics many years ago](https://xkcd.com/832/).  The customer said this program
should be "faster than a chess game", and a LUT will be very fast indeed.  One
approach that we could take is to translate this comic strip into some kind of
data structure in Python.  It would probably be some kind of multi-level list
or dictionary.  But that would be **very** tedious and error prone.  We are
very likely to make mistakes that will be hard to track down later.

Moreover, the customer insists that ML be a feature of the game... this is for
marketing instead of to solve any technological problem.  Indeed, because
Tic-Tac-Toe is such a small game with a trivial solution, ML can only slow it
down.  Perhaps they will be satisfied if we use ML to generate the LUT, freeing
us from doing it by hand.


### List all of the data that is used by the program, making note of where it comes from

For our part of the program, the information flow is very simple:

#### Output

The next move to take, an integer in the range 1-9, inclusive.


#### Input

A board state.  The program consider the current game board, and look into the
LUT for the best move to take at that juncture.

While a 2D list feels like the most natural data structure to represent a
Tic-Tac-Toe board, long experience has taught us that keeping things really
simple avoids bugs.  After some discussion among the AI team we have settled on
a 1D representation of the game.

Instead of

```python
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
```
we will go with this:

```python
board = (1, 2, 3, 4, 5, 6, 7, 8, 9)
```

It is structurally (and visibly) more compact, which helps to avoid syntax
errors.  We will also store the game board as a *tuple* instead of a *list*.
Tuples are like lists in every way, except that they are **immutable**.  When a
new game state is needed, instead of modifying the current list, a new one is
created from scratch.  This is a very valuable feature in a complicated program
like this; by restricting ourselves to read-only data structures we can avoid
all of the heartburn that comes from disparate parts of the program
unexpectedly changing a variable.  While it feels like this approach is less
efficient, consider that in a game of Tic-Tac-Toe there can be at most 9 state
changes.  Even if it takes an entire millisecond to create a new game board,
the total amount of time will still be shorter than what a human can perceive.

Also, this is a Python Tic-Tac-Toe game, not Doom Eternal; nobody expects 120
FPS in this game!


### Algorithms and formulae to be used

#### Generating the LUT

We need to create the LUT table used by the AI.  Since this Tic-Tac-Toe solver
has full knowledge of the game space, we'll name it the "Oracle".  One approach
we briefly considered was to hand-code the XKCD comic that realizes a
Tic-Tac-Toe oracle on paper.  But it proved very difficult to do this without
losing our place in the diagram, or making a transcription error.  It is also
possible that there is a bug in this diagram; we can't be sure that *every*
possible game outcome in the comic has been independently verified.  We would
need to write another program to test the correctness of our oracle.  At that
moment we realized that verifying the LUT is the same computational task as
solving the game in the first place.  This can be done with a minimax
algorithm, something we studied back in the day at USU when we took CS 5600
Intelligent Systems.



## Phase 1: Design
*(30% of your effort)*

We had one coordination meeting with the other team.  Well, it was wasn't so
much a meeting as it was a conversation over the Foosball table in the break
room.  Right after I burned one of their guys with a sick snake shot I told
them that the AI should be a function that gets passed to the function that
takes a turn for the CPU player.  I don't think anybody on their team had
written a function that takes a function as a parameter because they didn't
believe me that you can pass functions into functions.  But that's why we're
the AI team and they just make the UI.

While we are working on the minimax algorithm, the other team will need a
"dummy" AI function so they can test the 0 and 1 player game modes.  It is
really easy to give them a couple of dumb strategies for this purpose:

### Dumb strategy

This function needs a helper function `first_open_cell` that returns the ID of
the first open cell on the Tic-Tac-Toe board.  That helper, in turn, needs
another helper that makes a list of **all** open cells on a game board.  We'll
call that helper `open_cells`.

In the Foosball meeting we learned that they also need the `open_cell`
function.  Instead of waiting for them to get around to writing it, we just
made our own.

```python
open_cells(b):  -> return tuple of open cells on the board 'b'
    initialize cs to an empty list
    for each cell on the board:
        if cell is an integer:
            append cell to list cs
    return cs, converted to a tuple


first_open_cell(b):  -> return the ID of the first open cell on the board 'b', or None if the board is full
    initialize cs to the list returned by open_cells(b)
    if cs is empty
        return None
    else
        return cs[0]


strategy_dumb(b):  -> returns first open cell on the board 'b'
    return first_open_cell(b)
```

`strategy_dumb()` will return `None` if the Tic-Tac-Toe board is full; but that
should not occur in a real game because a full board would mean the game is over.


### Random strategy

This function uses the `choice` function from Python's built-in `random`
module.

```python
strategy_random(b):  -> return the ID number of an open cell at random
    return choice(open_cells(b))
```

If it happens that NO squares are left, this function will raise `IndexError`.
However, that should never happen in a "real" game; at least one square is
always open when a strategy function is called.  A full board will be detected
as a "draw", and the game will return to the main menu.



### Oracle strategy

The question before us is "how to associate a board state (a tuple) with the
number of the best cell to mark?".

We considered many alternatives for this function before settling on our
present design.  The LUT is simply an array that contains all possible board
states in Tic-Tac-Toe.  The input to this function is the current board state,
a tuple.  This function will scan the LUT for a match with the current game
board:

```python
if b in LUT:
    # now turn this into a next move
```

Somehow, the match must indicate which cell is the best next move.

We considered nesting another list within the LUT - each element of the LUT is
a 2-tuple where the first sub-element is a board and the second element is the
next best move, like this:

```python
LUT = (
        ...
        ((1, 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'O'), 0),
        ((1, 'X', 'O', 'X', 'O', 'X', 'X', 'O', 9), 0),
        ((1, 'X', 'O', 'X', 'O', 'X', 'X', 8, 'O'), 1),
        ((1, 'X', 'O', 'X', 'O', 'X', 7, 'X', 'O'), 2),
        ((1, 'X', 'O', 'X', 'O', 'X', 7, 8, 'O'), 3),
        ...
        )
```

The lookup code would be more complicated:

```python
for p in LUT:
    if p[0] == b:
        return p[1]
```

We didn't like how this made the LUT look, and the extra subscripts `[0]` and
`[1]` are just... arbitrary.

Our next idea was to use parallel arrays - two arrays whose values at the same
subscript are related.  We would use the LUT's `.index()` method to return the
position of the game board.  Then, the value of that index in the companion
array would indicate the best move:

```python
LUT = (
        ...
        ('X', 2, 'X', 'O', 'X', 'O', 7, 8, 9),
        ('X', 2, 'X', 'O', 5, 'O', 'X', 'O', 9),
        ('X', 2, 'X', 'O', 5, 'O', 'X', 8, 'O'),
        ('X', 2, 'X', 'O', 5, 'O', 'O', 'X', 9),
        ('X', 2, 'X', 'O', 5, 'O', 7, 'X', 'O'),
        ...
        )

MOVES = (..., 2, 2, 2, 2, 2, ...)

best = LUT.index(('X', 2, 'X', 'O', 5, 'O', 'O', 'X', 9))
return MOVES[best]
```

We didn't like this approach because we know the LUT is going to have thousands
of elements, and thus take a lot of space in the source code.  Adding another
extremely long array to the program is asking for trouble.

The approach we have settled on is a compromise of the two: we split the LUT
into 9 sub-tables, each of which contains board states sharing the same
response.  The sub-table of states with a best response of `1` is stored at
position `0` in the LUT, states with a best response of `2` are filed under
position `1`, and so on.  This way, the information of the parallel array is
"baked-in" to the LUT.  Whoever uses the LUT just needs to remember that the
answers are off by one.

This adds just one extra `for` loop to the lookup code, which is a good
compromise.

```python
LUT = (
    ( # best move is `1`
        (1, 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'O'),
        (1, 'X', 'O', 'X', 'O', 'X', 'X', 'O', 9),
        (1, 'X', 'O', 'X', 'O', 'X', 'X', 8, 'O'),
        (1, 'X', 'O', 'X', 'O', 'X', 7, 'X', 'O'),
        (1, 'X', 'O', 'X', 'O', 'X', 7, 8, 'O'),
        ...
        ),
    ( # best move is `2`
        ('X', 2, 'X', 'O', 'X', 'O', 7, 8, 9),
        ('X', 2, 'X', 'O', 5, 'O', 'X', 'O', 9),
        ('X', 2, 'X', 'O', 5, 'O', 'X', 8, 'O'),
        ('X', 2, 'X', 'O', 5, 'O', 'O', 'X', 9),
        ('X', 2, 'X', 'O', 5, 'O', 7, 'X', 'O'),
        ...
    ),
    ...
)

for i in range(len(LUT)):
    for j in range(len(LUT[i])):
        if b == LUT[i][j]:
            return i
```



## Phase 2: Implementation
*(15% of your effort)*

An early version of `strategy_oracle()` used `LUT[i].index()` to find the
current game board instead of a second `for` loop.  But it turns out that when
`LUT[i]` **does not** contain the current state, instead of just returning
`False` or `None`, `.index()` raises `IndexError`, which crashes the program.
We tried **exception handling** to prevent the program from crashing, but this
ended up making the AI run a bit slower.  We learned that exception handling
should not be used in situations that are not actually exceptional.



## Phase 3: Testing & Debugging
*(30% of your effort)*

The Oracle AI is predictable; for any given game state, it has but one
response.  To test that it is playing optimally, start a one player game and
make **exactly** the moves stated below.  The games should play out precisely
as documented here:

### A Human playing as 'X':

*   Open with 1
    *   O plays 5
    *   Respond with 7
    *   O plays 4
    *   Respond with 6
    *   O plays 2
    *   Respond with 8
    *   O plays 9
    *   Respond with 3, drawing the game
*   Open with 2
    *   O plays 1
    *   Respond with 5
    *   O plays 8
    *   Respond with 7
    *   O plays 3
    *   Respond with 6
    *   O plays 4
    *   Respond with 9, drawing the game
*   Open with 3
    *   O plays 5
    *   Respond with 9
    *   O plays 6
    *   Respond with 4
    *   O plays 1
    *   Respond with 8
    *   O plays 7
    *   Respond with 2, drawing the game
*   Open with 4
    *   O plays 1
    *   Respond with 5
    *   O plays 6
    *   Respond with 2
    *   O plays 8
    *   Respond with 3
    *   O plays 7
    *   Respond with 9, drawing the game
*   Open with 5
    *   O plays 1
    *   Respond with 2
    *   O plays 8
    *   Respond with 3
    *   O plays 7
    *   Respond with 9
    *   O plays 4, winning the game
*   Open with 6
    *   O plays 3
    *   Respond with 5
    *   O plays 4
    *   Respond with 9
    *   O plays 1
    *   Respond with 7
    *   O plays 2, winning the game
*   Open with 7
    *   O plays 5
    *   Respond with 1
    *   O plays 4
    *   Respond with 6
    *   O plays 2
    *   Respond with 8
    *   O plays 9
    *   Respond with 3, drawing the game
*   Open with 8
    *   O plays 2
    *   Respond with 5
    *   O plays 1
    *   Respond with 3
    *   O plays 7
    *   Respond with 6
    *   O plays 4, winning the game
*   Open with 9
    *   O plays 5
    *   Respond with 7
    *   O plays 8
    *   Respond with 3
    *   O plays 2, winning the game


### A Human playing as 'O':

*   X opens with 1
    *   Respond with 3
    *   X plays 4
    *   Respond with 7
    *   X plays 5
    *   Respond with 6
    *   X plays 9, winning the game
*   X opens with 2
    *   Respond with 8
    *   X plays 1
    *   Respond with 3
    *   X plays 7
    *   Respond with 4
    *   X plays 5
    *   Respond with 9
    *   X plays 6, drawing the game
*   X opens with 3
    *   Respond with 4
    *   X plays 1
    *   Respond with 2
    *   X plays 5
    *   Respond with 7
    *   X plays 9, winning the game
*   X opens with 4
    *   Respond with 9
    *   X plays 7
    *   Respond with 6
    *   X plays 1, winning the game
*   X opens with 5
    *   Respond with 6
    *   X plays 1
    *   Respond with 9
    *   X plays 3
    *   Respond with 2
    *   X plays 7, winning the game
*   X opens with 6
    *   Respond with 9
    *   X plays 1
    *   Respond with 7
    *   X plays 8
    *   Respond with 3
    *   X plays 5
    *   Respond with 4
    *   X plays 2, winning the game
*   X opens with 7
    *   Respond with 8
    *   X plays 1
    *   Respond with 4
    *   X plays 3
    *   Respond with 5
    *   X plays 2, winning the game
*   X opens with 8
    *   Respond with 9
    *   X plays 1
    *   Respond with 6
    *   X plays 3
    *   Respond with 2
    *   X plays 7
    *   Respond with 4
    *   X plays 5, winning the game
*   X opens with 9
    *   Respond with 8
    *   X plays 3
    *   Respond with 6
    *   X plays 1
    *   Respond with 2
    *   X plays 5, winning the game


## Phase 4: Deployment
*(5% of your effort)*

Code was submitted on-time and without problems!

Before turning in our contribution to the project we deleted all of the minimax
algorithm code, since that was not meant to be part of the finished product.
In the end, the minimax algorithm was much faster than expected, and we could
have just left it in.  The program would have been a lot shorter if we had!

But, the customer is obsessed with machine learning.  So we re-named the LUT to
`MODEL` in the code to reassure them that a machine taught itself how to play
Tic-Tac-Toe.

We ran some benchmarks at the end to see how fast our oracle is.  The results
blew us away:

*   The oracle can play 123 games against itself in .24 seconds, which is how
    long it takes to run `import numpy`
*   The oracle can play 546 games against itself in 1.07 seconds, which is how
    long it takes to run `import torch`
*   The entire LUT is 4,540 lines of Python code and weighs in at only 246 Kb.
    That's close to the size of Python's `turtle` library!


## Phase 5: Maintenance

### What parts of your program are sloppily written and hard to understand?

The functions are short and clean.  However, the LUT itself is really, really
long.  If one doesn't understand how the LUT is constructed, they will find it
to be confusing.  It does not lend itself to being edited by hand.  When we
found that changes were necessary, it was much easier to edit the program that
makes it and re-generate from scratch.


#### Are there parts of your program which you aren't quite sure how/why they work?

We are confident that we understand all of this.


#### If a bug is reported in a few months, how long would it take you to find the cause?

If there is a mistake in the LUT, it would take quite a while to dig through it
to locate it.

The other functions are all very short and straightforward; we can find a
problem in under half an hour.


### Will your documentation make sense to anybody besides yourself?

We intentionally avoided using AI / ML jargon to keep the doc strings
accessible to entry-level programmers.  In some cases the doc strings are much
longer than the code they describe!  We do not anticipate any misunderstandings
from a programmer with moderate Python training.

### Will your documentation make sense to yourself in six month's time?

Yes.

### How easy will it be to add a new feature to this program in a year?

Because there is little code, adding features ought to be simple.  The bigger
challenge would be adding a feature that depends on the LUT being in a
different format (say, if the game state is represented as a 2D tuple instead
of 1D).  That would require major changes to the minimax algorithm which
generates the LUT, and a rewrite of the `strategy_oracle()` function.

### Will your program continue to work after upgrading your computer's hardware?

Yes - nothing here depends on specialized hardware.  We couldn't make this
guarantee if we used *real* machine learning that needed an NVidia board, or
something exotic like that.

### Will your program continue to work after upgrading the operating system?

Yes - there is no platform-specific code in this program.

### Will your program continue to work after upgrading to the next version of Python?

Yes - we intentionally restricted ourselves to using very basic features of the
language.  In fact, our code even works in Python 2.7!  (Just don't ask us why
we know this)
