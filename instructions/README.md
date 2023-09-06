# CS 1440 Assignment 1: Tic-Tac-Toe - Instructions

*   [How to Do This Assignment](#how-to-do-this-assignment)
    *   [Phase 0: Requirements Analysis](#phase-0-requirements-analysis)
    *   [Phase 1: Design](#phase-1-design)
    *   [Phase 2: Implementation](#phase-2-implementation)
    *   [Phase 3: Testing and Debugging](#phase-3-testing-and-debugging)
    *   [Phase 4: Deployment](#phase-4-deployment)
    *   [Phase 5: Maintenance](#phase-5-maintenance)
*   [What We Look for When Grading](#what-we-look-for-when-grading)
*   [Important Things to Watch Out For](#important-things-to-watch-out-for)


## How to Do This Assignment

The flaw in this program is that the optimal AI player can lose.  It is your job to find out why.  You will uncover the causes as you study the code.  If you think anything else which looks wrong, **just leave it alone**.  I will make a public announcement if another serious issue is discovered.  Apart from the AI bug, I am confident this program works as intended.


### Phase 0: Requirements Analysis
*(20% of your effort)*

**Important - do not change any code in this phase**

0.  Read the [Project Requirements](./Requirements.md) to orient yourself with the project.
1.  Study the *Software Development Plans* written by the previous teams to learn what they accomplished.
    *   [AI team's SDP](./AI_Team_Plan.md)
    *   [Game Engine team's SDP](./Engine_Team_Plan.md)
    *   You should understand these documents well enough to find your way around the source code.
    *   Pay special attention to the test cases they wrote.
2.  Run the program several times and try to identify which functions perform what actions.
    *   **Do not change the source code in this phase of the project!**
        *   You will edit code in **Phase 2: Implementation**.
        *   In this phase your task is to *draft* the plan that you will follow when you get there.
3.  Identify functions that were written under *faulty assumptions* and produce *incorrect results*.
    *   **Do not rewrite these functions now!**
    *   You will need to re-design these functions to fix the bug in the program.
    *   In this phase you need only to locate which ones are faulty.
4.  This project starts with **one** Python module that contains all of the code.
    *   At the end of the project you will have reorganized the code into **five** modules.
    *   The **five** modules will have these names and contents:
        1.  `ttt.py` - the main entry point of the program; ties everything together.
            *   Will consist of a few import statements and a `__name__ == '__main__'` block
            *   This module will not contain any function definitions (i.e. the `def` keyword does not appear in this module)
        2.  `interface.py` - code that prints pretty output and takes user input.
            *   This is the only module in the project where the `input()` function is called.
            *   Most (but not all) of the functions that call `print()` belong in this module.
            *   Functions returning strings with terminal escape sequences belong here
        3.  `engine.py` - this module is for functions that drive the main game loop.
            *   There are four different game loops, each corresponding to a player selection mode (i.e. CPU vs. CPU, human vs. CPU, CPU vs.  human, human vs. human)
            *   This code controls how players take turns.
            *   Functions in this module *may* output messages with the help of other functions defined in `interface.py`.
        4.  `ai.py` - holds the strategy functions which power the CPU opponent, and data they use.
        5.  `util.py` - miscellaneous, low-level utility functions.
            *   Functions belonging to this module are so simple that they don't require other imports (i.e. this module needs no `import` statements).
            *   Some of the functions that belong to this module must be modified to change representation of the game board.
            *   These functions do not print anything, nor take input directly from the user.
5.  Take the **Starter Code Quiz** on Canvas.
    *   Do not worry if you can't answer all of the questions yet
    *   You can re-take the quiz as many times as you want before the assignment is due
6.  Track your time in Signature.md.


### Phase 1: Design
*(30% of your effort)*

**Important - do not change any code in this phase**

0.  Locate functions that are *redundant* or *serve no purpose* in the program; these must be deleted in the next phase.  There are a few exceptions to this:
    *   Unused AI strategy functions *may* be kept for testing.
    *   Unused color functions *may* be kept for future development.
1.  Redesign faulty functions on paper; **don't rewrite the Python code yet**.
    *   Sketch out improved versions of these functions in *pseudocode*.
    *   Walk through the pseudocode in your head, with a pad of paper or a whiteboard to convince yourself that your changes will work.
2.  You may write *some* runnable Python code to test out your ideas.
    *   This is called *prototyping*, and is a normal part of the design process.
    *   Do not become too attached to your prototype!
    *   Be prepared to delete prototype code after this phase.
    *   It helps to *not* write prototype code in the same files as *real* code.
3.  Consider if any new test cases could be devised that ensure the new program will perform correctly.
4.  You should be able to get 100% on the **Starter Code Quiz** by now.
5.  Track your time in Signature.md.


### Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

0.  Reorganize the program's functions into the **five** modules described above.
    *   Now is the time to create four *new* Python modules in `src/`
    *   Give the files these names (mind the capitalization!):
        1.  `interface.py`
        2.  `engine.py`
        3.  `ai.py`
        4.  `util.py`
1.  **Rewrite** faulty, incorrect functions so they perform correctly.
    *   You may rename variables and functions to improve readability.
2.  **Delete** functions that do not have a use (subject to the exceptions outlined above).
3.  By the end of this phase the program is runnable.
    *   **Do not** move on if your program crashes regularly!
4.  Track your time in Signature.md.


### Phase 3: Testing and Debugging
*(30% of your effort)*

0.  Run through the test cases suggested by the previous teams.
1.  Run through any new test cases that you devised.
2.  If you found bugs in this phase, explain what was wrong and how you fixed it.
3.  Track your time in Signature.md.


### Phase 4: Deployment
*(5% of your effort)*

It is your responsibility to ensure that your program will work on your grader's computer.

*   Code that crashes and *cannot* be quickly fixed by the grader will receive **0 points** on the relevant portions of the rubric.
*   Code that crashes but *can* be quickly fixed by the grader (or crashes only *some* of the time) will receive, at most, **half-credit** on the relevant portions of the rubric.

The following procedure is the best way for you to know what it will be like when the grader runs your code:

0.  Review [How to Submit this Assignment](./How_To_Submit.md) and make sure that your submission is correct.
1.  Push your code to GitLab, then check that all files and commits are there.
2.  Clone your project into a *different directory* on your computer and re-run your test cases.


### Phase 5: Maintenance

**Before The Due Date**

0.  Review your Signature.md one last time.
1.  Make one final commit and push your **completed** Signature.md to GitLab.
2.  Make sure that you are happy with your **Starter Code Quiz** score.

**After You Submit (Can Happen After The Due Date)**

0.  Respond to the **Assignment Reflection Survey** on Canvas.
1.  Submit a **Code Review** video to Canvas.


## What We Look for When Grading

**Total points: 60**

*   Program behavior (25 points)
    *   AI opponent is unbeatable
        *   CPU vs. CPU matches always end in a draw
        *   Human vs. CPU matches end either in a draw or CPU victory
    *   Existing good behavior of program is preserved
        *   The user interface and appearance is unchanged from the starter code
        *   The Easter Egg is still accessible just as it was in the original program
    *   No new bugs are introduced
        *   Program doesn't crash
        *   Illegal user input is detected by the program and an appropriate error message is displayed
    *   All test cases work as expected
*   Code quality (20 points)
    *   Functions are organized into the correct modules
    *   No useless variables or constants remain
    *   Useless functions are removed
        *   Exceptions
            *   Unused AI strategy functions *may* be kept for testing
            *   Unused color functions *may* be kept for future development
        *   No duplicated or redundant code remains; each function is present in only one module
    *   Doc strings and comments match the code they describe
    *   Representation of the game board (number of dimensions) is consistent throughout the program
    *   Import statements are reasonable
        *   No useless import statements are present
        *   Program *does not* import any modules **except**:
                *   `random`
                *   `time`
                *   `typing`
                *   modules you wrote yourself
        *   No import statement fail due to misspelling or incorrect capitalization.
            *   **Windows users** make sure that the capitalization of file names on GitLab match your `import` statements!
        *   No imports involve the `src.` package; this is the result of a PyCharm misconfiguration
*   Repository Structure (10 points)
    *   `.gitignore` is correct and no forbidden files or directories are present
    *   The repository is a clone of the starter code
    *   The repository's GitLab URL follows the naming convention
    *   All required files and directories are in their expected locations
*   Time management (5 points)
    *   Signature.md contains accurate information about the time you spent on this project
        *   The time reported on the **TOTAL** entry is the sum of the daily entries
    *   The *TODO* message and the placeholder entries have been removed
