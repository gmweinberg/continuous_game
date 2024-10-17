#!/usr/bin/env python

from continuous_game.game import Game
from continuous_game.strategy import Strategy
from continuous_game.util import zero_sum

def score_pistol(t1, t2):
    """A score function for the pistol_duel game"""
    if t1 < t2:
        return zero_sum(t1 - (1-t1)*t2)
    else:
        return zero_sum((1-t2)*t1 - t2)

def get_max_dom(strat1):
    """Find the maximum constant strategy that is dominated by strat."""
    max_ = 0
    for ii in range(1000):
        val = ii * 0.001
        strat2 = Strategy(val)
        if not pistol_game.dominates(strat1, strat2):
            break
        max_ = val
    print("max_ is {}", max_)


if __name__ == '__main__':
    from argparse import ArgumentParser
    from ast import literal_eval
    parser = ArgumentParser()
    parser.add_argument("--max_", help="find max const strategey dominated by max", default=None)
    args = parser.parse_args()
    pistol_game = Game(score_pistol)
    #pistol_game.verbose = True
    if args.max_ is not None:
        try:
            dist = literal_eval(args.max_) # this should be a probability dict
        except Exception:
            dist = float(args.max_) # or maybe a floart, if this doen't work give up
        strat = Strategy(dist)
        get_max_dom(strat)
    else:
        strat1 = Strategy({0.45:0.5, 1:0.5}) 
        strat2 = Strategy(0.22)
        print(pistol_game.dominates(strat1, strat2))
        print('hello')

# ./test_pistol.py --max "{0.43:0.5, 0.82:0.5}"
