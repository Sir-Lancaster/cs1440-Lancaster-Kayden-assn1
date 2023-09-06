# CS 1440 Assignment 1: Tic-Tac-Toe - How to Submit this Assignment

* [When to Submit Your Work](#when-to-submit-your-work)
* [Repository Naming Convention](#repository-naming-convention)
* [Repository Layout](#repository-layout)
* [How to Verify Your Submission](#how-to-verify-your-submission)
* [Python Version](#python-version)


I am very particular about the format of your assignment submissions.

*   Yes, I have my reasons.
*   No, I do not make exceptions.
*   Deviations from these guidelines **will result in penalties**.


<details>
<summary><strong>Why am I so picky about how you submit your homework?</strong></summary>

0.  **Programming is a detail-oriented activity**.  The sooner you embrace this fact, the happier you will be.
1.  In the workforce **your boss and coworkers will be just as picky as I am** about how you turn in your work.  Perhaps more so.  It is not good enough if your code "just works" on your computer.  You code needs to "just work" on their computers, too.
2.  In a large class **every second adds up**.  If it takes 60 seconds for a grader to figure out how to run a student's submission, then in a class of 180 students three hours is spent just getting started.  There are eight assignments in this class; we spend the equivalent of three whole work-days every semester on this trivial detail.

</details>



## When to Submit Your Work

*   Assignments are due by 11:59:59 PM on the posted due date according to the clock on my GitLab server.
*   A submission arrives when it is *pushed* to my GitLab server.
    *   Commits pushed _after_ the due date are late.
    *   Commits bearing timestamps _before_ the due date but are *pushed* _after_ the due date are late.
*   You can push your code to GitLab as many times as you want.
    *   Do not push your code to GitLab after the due date passes *unless* you intend to turn it in late.
*   Per the **Grace Period** policy explained in the syllabus, you can continue working on your assignment until the start of the next lecture following the due date.  After that moment, no new pushes will be graded.


### Which clock judges lateness?

The clock on **gitlab.cs.usu.edu** keeps the official time for the class.  When you push to the server you will see a "receipt" in your console:

```
***********************************************************************
*           __  ________  __  _____                ____    _          *
*          / / / / __/ / / / / ___/__  __ _  ___  / __/___(_)         *
*         / /_/ /\ \/ /_/ / / /__/ _ \/  ' \/ _ \_\ \/ __/ /          *
*         \____/___/\____/  \___/\___/_/_/_/ .__/___/\__/_/           *
*                                         /_/                         *
*  ,/         \,                                                      *
* ((__,-"""-,__))                                                     *
*  `--)~   ~(--`                                                      *
* .-'(       )'-,                                                     *
* `--`d\   /b`--`  Big Blue says:                                     *
*     |     |                                                         *
*     (6___6)  Your submission arrived Wed 18 Jan 2023 21:17:25 MDT   *
*      `---`                                                          *
*                                                                     *
***********************************************************************
```

*   The time stamp comes from the GitLab server's clock.
*   This is the official time of your submission's arrival.
*   If you don't see this receipt, make sure that you are pushing your code to **my** GitLab server at `gitlab.cs.usu.edu`.



## Repository Naming Convention

I wrote a program that helps me find your submission out of the thousands on GitLab.  It is important that the name of your repo follows this pattern:

`cs1440-lastname-firstname-assn#`

*   Use hyphens `-` to separate words.  **Do not** use underscores `_`, dots `.` or other punctuation.
*   Include the course number with `cs` at the front.
*   Name your submission such that _lastname_ and _firstname_ correspond to your "Full Name" in Canvas.  Find your "Full Name" in Canvas by browsing to `Account -> Settings`.
    *   Two first or last names can be used; separate them with hyphens `-`.
    *   You may include your middle name.
*   Put the assignment number after `assn#`
    *   **Do not** use any other variation of the word "assignment".

#### Good repo names:

*   `cs1440-rubio-gould-teresa-assn2` (Teresa Rubio-Gould's Assignment #2 - multiple names are OK)
*   `cs1440-jones-bill-assn4` (Bill Jones's Assignment #4)

#### Bad repo names:

*   `cs1000-smith-jane-assn1` (invalid course number: this is **cs1440**, not **cs1000**)
*   `1440-jones-bill-assn4` (invalid course number: does not begin with **cs**)
*   `cs-1440-jones-bill-assn4` (invalid course number: spell it **cs1440**, not **cs-1440**)
*   `cs1440-rubio-gould-teresa-ass2` (**assn#** is spelled wrong)
*   `cs1440-rubio-gould-teresa-assn-2` (**assn#** is spelled wrong)
*   `cs1440-rubio-gould-teresa-assign2` (**assn#** is spelled wrong)
*   `cs1440-pixelwarrior5010-assn2` (**pixelwarrior5010** isn't your "Full Name" in Canvas)
*   `cs1440.jones.bill.assn4` (periods instead of hyphens)

When you get these details wrong it appears that you made no submission at all.

On the other hand, you may create repositories for your other courses on my GitLab server.  This naming convention avoids confusion between those repositories and your homework for this course.


<details>
<summary><strong>Rationale</strong></summary>

0.  Naming your GitLab project with your Canvas name avoids confusion.  Some graders are not native English speakers and don't know that `Dick == Richard`, `Lexi == Alexandria`, `Billy == William`, `Chuck == Charles`, `Becky == Rebecca`, etc.
1.  The naming convention is rigid because the program I wrote to find your repo by its URL is very simple and is easily confused.
2.  Your project's *name* on GitLab can differ from its *path* or URL.  If you made a mistake while naming it, make sure that you change its **Path** instead of its **Name**.  *See below*

</details>


### Changing your repository's URL on GitLab

If you gave your repo the wrong name, you can fix it in GitLab before the due date and receive **no penalty**.

0.  Open the repo's settings in GitLab by hovering over the gear icon in the left sidebar and clicking `General`
1.  Scroll all the way to the _bottom_ and expand the **Advanced** section.  _Do not bother changing the **Project Name** that you see at the top of this page!_
2.  Scroll all the way to the _bottom_ of the **Advanced** section until you see a box titled **Change path**.  Put the correct name into this box and save your changes.
3.  Back on your PC update your repo's remote URL.  Assuming your GitLab remote is nicknamed `origin`, a command like this will update the URL (substitute your own details in this command):
    ```
    git remote set-url origin git@gitlab.cs.usu.edu:YOUR_USERNAME/cs1440-YOUR-NAME-AND-ASSIGNMENT
    ```
4.  After changing the repository URL you *must* make another push before my submission detection program will notice the change.  Make a trivial change so that you can do a new push.  A small cosmetic change in one of the Markdown files is good enough.



## Repository Layout

0.  **Do not start from scratch**
    *   Clone the starter code repository and continue from there.
1.  A well-organized submission makes it **easy for us to help you** and grade your work.
    *   Some files and directories **are required** to be present.
    *   Some files and directories **must not** be part of your submission.
    *   **Do not** remove or re-arrange files given to you in the starter code unless told to do so.
2.  This is what a good submission looks like:
    *   ```
        cs1440-assn0
        |-- .gitignore
        |-- doc
        |   `-- Signature.md
        |-- instructions
        |   |-- AI_Team_Plan.md
        |   |-- Engine_Team_Plan.md
        |   |-- How_To_Submit.md
        |   |-- README.md
        |   `-- Requirements.md
        |-- README.md
        `-- src
            |-- ai.py
            |-- engine.py
            |-- interface.py
            |-- ttt.py
            `-- util.py
        ```


### Files and directories your repository _MUST_ contain

0.  A `README.md` in the top-level directory
    *   This file is *not* read-only, and you *may* modify it
    *   If you have any special instructions or explanations for your grader, put them at the top of this file
1.  A file named `.gitignore`.  This file may be hidden from file listings in the shell
    *   The contents of `.gitignore` are explained in detail below
2.  `src/`
    *   Contains your source code
3.  `instructions/`
    *   Contains my instructions to you
    *   Don't modify files in this directory; consider this area read-only
4.  `doc/`
    *   Contains documentation written by you.  You may edit the files provided by us, and add new ones
    *   `Signature.md` - the *Sprint Signature*
        *   Record a **brief** log of your accomplishments every day that you worked on the assignment
        *   One or two sentences per day suffice
    *   Keep this directory **tidy**
        *   Delete extraneous and out-of-date files so your grader doesn't have to waste time figuring out what's what


### Files and directories your repository _MAY_ contain

0.  `.idea/` created by PyCharm
1.  `.vscode/` created by Visual Studio Code
2.  Any other subdirectories needed to organize your work as you see fit


### Files your repository _MUST NOT_ contain

0.  Directories containing pre-compiled files or other generated files created by your IDE or build tools (e.g. `venv`, `*.pyc`, etc.)
1.  Zip files or archives
2.  Backup files or folders
3.  Screenshots
4.  Any other detritus left behind from your experimentation
5.  Extremely large files.  What is considered "extremely large" depends upon the project, but a good rule of thumb is to avoid committing files larger than 20 megabytes

**Before you make your final submission, clean up your repository!**


### Block unwanted files with `.gitignore`

`.gitignore` helps you avoid committing unwanted files and directories to your repository.  `.gitignore` is a plain text file.  Each line specifies a filename pattern that Git refuses to add to the repository.  The starter code already includes a `.gitignore` file with these contents:

```
venv
.DS_Store
__pycache__
*.pyc
*.csv
*.zip
*.bak
*.png
```

If you must recreate this file yourself, understand that Git is *very* particular about the spelling of this file's name.  It must be spelled *exactly* as `.gitignore`.

*   The file name starts with a dot `.`
*   All lowercase
*   No file extension at the end

Git does *not* treat names as ignore files:

*   `gitignore` (does not **start with a dot**)
*   `.gitignore.txt` (ends in **.txt**)
*   `.Gitignore` (wrong capitalization)
*   `.GITIGNORE` (wrong capitalization)

Some text editors on Windows will not save files with names that start with `.`.  Sometimes an extension such as `.txt` is automatically added to the end of your new file's name.  The most convenient way to create `.gitignore` on Windows is from the Bash command line with this command:

```
nano .gitignore
```

Paste the contents shown above, one entry per line.  When you are done press `Ctrl-X` (a.k.a. `^X`) to exit Nano and follow the on-screen prompts to save the file.


<details>
<summary><strong>Rationale</strong></summary>


### What difference do the names and locations of my files make?

*   The starter code repository is organized to help you quickly find files in the project.
*   Your boss and coworkers will expect you to follow their organization at your job.
*   Your instructor, TAs and coaches will be able to run your program without fuss when you seek help, and see exactly the same output that you do.
*   This layout facilitates quick and efficient grading.


### Why do I need to write **doc/Signature.md**?

*Don't Git's commit messages make this file redundant?*

No.  Git commit messages serve a different purpose than the Sprint Signature.

*   Git commit messages describe just a small portion of your work, often just a few lines of code.
    *   You should make several commits each day, each with its own message.
*   The Sprint Signature captures a big-picture summary of your daily work, and helps you stay on-task:
    *   If your daily summary consists of pointless fiddling, you will be more focused tomorrow.
    *   Reviewing the sprint signature helps you recognize when you are getting stuck in the project.
*   Writing a daily log encourages you to work at least a little bit every day, helping you become consistent.


### Do you even look at these files?

Yes.

</details>



## How to Verify Your Submission

Sometimes there are files on your computer that are not committed to Git.  Consequently, those files are not present when we clone your repository, which causes your program to crash.

An easy way to avoid this is to re-clone your repository from GitLab into a fresh location on your computer and give it one final test from there.  This lets you experience your submission just as the graders will.

0.  In your shell, navigate into a different directory and `git clone` your repository.
    *   You can find the URL on to clone by running `git remote -v` in your original repository, or on the GitLab website.
1.  Prevent *Gitception* by not `git clone`ing when your shell is already inside a Git repo.
    *   *Always* run `git status` before using `git clone`!  You want it to show you this error:
    *   ```
        $ git status
        fatal: Not a git repository (or any parent up to mount point /)
        Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
        ```
2.  Thoroughly test this fresh copy of your program:
    *   Run your program from the command-line instead of your IDE; we don't grade your code with an IDE.
    *   Run the command-line examples shown in the instructions.
    *   Run any tests included with the starter code.
    *   Run through the test cases in the **Testing** sections of the other teams' SDPs.



## Python Version

*   Graders will run your code against the official distribution of Python version 3.8 or greater from https://python.org
*   Python version 2 has reached its end of life.
*   Code written for Python 2.x is not acceptable in this class.

For this class you must either:

*   Install Python version 3.8 or greater on your own computer
*   Find a computer with the correct version of Python
    *   Computers in CS labs and the Engineering Computer lab have the correct version of Python.


### How can I tell if I have the right version of Python installed?

Run `python --version` from the command line:

```
$ python --version
Python 3.9.16
```

If this reports a version number beginning with 2, run `python3` instead:

```
$ python3 --version
Python 3.9.16
```
