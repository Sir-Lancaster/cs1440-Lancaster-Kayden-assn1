
# Import ai Statements
import ai

# Import Engine Statements
import engine

#import interface statements
import interface

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




CPU_DELAY = 0.75




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
        interface.logo()
        mode = interface.player_select()
        if mode == 0:
            engine.cpu_vs_cpu(ai.strategy_oracle, ai.strategy_oracle)
        elif mode == 1:
            engine.human_vs_cpu(ai.strategy_oracle)
        elif mode == 2:
            engine.cpu_vs_human(ai.strategy_oracle)
        elif mode == 3:
            engine.human_vs_human()
        elif mode == 4:
            engine.game(ai.strategy_oracle, ai.strategy_oracle)
        else:
            break
    print("Thanks for playing!")
