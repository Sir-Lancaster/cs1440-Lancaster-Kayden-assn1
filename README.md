# CS 1440 Assignment 1: Tic-Tac-Toe

*   [Instructions](./instructions/README.md)
    *   [How to Submit this Assignment](./instructions/How_To_Submit.md)
*   [Project Requirements](./instructions/Requirements.md)
    *   [AI team Software Development Plan](./instructions/AI_Team_Plan.md)
    *   [Game Engine team Software Development Plan](./instructions/Engine_Team_Plan.md)


*Note: you may replace text in this file with your own notes.  For example, when seeking help from TAs or tutors replace this text with a description of your problem and push it to GitLab.*


## Get the starter code

*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$` (that represents your shell's prompt).
    *   Replace `USERNAME` with your GitLab username, `LAST` and `FIRST` with your names as used on Canvas.

```bash
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn1 cs1440-assn1
$ cd cs1440-assn1
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn1.git
$ git push -u origin --all
```


## Overview

In the midst of the hype surrounding AI-generated art and text-adventure games, a group of investors contracted DuckieCorp to build an unbeatable Tic-Tac-Toe game (they have obviously never seen the 1983 Matthew Broderick movie "WarGames", but who are we to turn down an easy job?)

The customer specifically asked for a Tic-Tac-Toe engine that incorporates machine learning.  So, our AI team immediately got to work with NumPy and PyTorch and by lunchtime realized that was a really dumb way to make a Tic-Tac-Toe game.  I believe our lead AI engineer just translated [this diagram](https://xkcd.com/832/) into Python.  Now we have a Tic-Tac-Toe AI that can't be beat!

Meanwhile, our UI team got to work on a text interface for the prototype.  I think they had too much fun with it.  I heard rumors that they hid an *Easter Egg* in there.  Everything was going great until the two teams combined their code into one program.  For some reason, that made the unbeatable AI become *really* stupid.  The meetings that followed were a disaster.  There was a lot of screaming, name-calling and chair-throwing.  It was the most drama that DuckieCorp has ever seen!  As a result, some of our engineers are on involuntary PTO while they cool down.

This is where you come in.  Because the project became so toxic, none of the other engineers will have anything to do with it.  As the brand-new intern, you're not really in a position to push back against your boss, are you?  While yours is an unpaid position, just think of the respect you can earn by swooping in and saving the project!  And if the original programmers hate you for showing them up, well, you'll be on your way in a few months anyhow.

I wasn't kidding when I said that our engineers *immediately* got to work on this project.  Here at DuckieCorp we ordinarily begin a project with a *sprint kickoff meeting* to get everybody on the same page.  This time our engineers were so eager to get started that they barely coordinated with each other.  In hindsight, this was a huge red flag.

Your first order of business is to untangle the mess that the code has become by splitting the project into modules.  Once you do that, I think the AI bug will just jump out at you.  Good luck!


## Running the starter code

You can play the game from the top directory of the repository like this:

```bash
$ python src/ttt.py
```

If that gives you `Command not found`, try `python3` instead.

You can change which AI the CPU player uses by editing the starter code.  You might want to do this while testing the program.  Scroll to the bottom of `src/ttt.py` and look for the relevant bits of code under `if __name__ == '__main__':`.  The available AI's are:

0.  `strategy_dumb` - plays the first open square
1.  `strategy_random` - plays a random open square
2.  `strategy_oracle` - has full knowledge of every possible move in every possible game; it *should* play optimally, but presently it seems to pick moves at random
