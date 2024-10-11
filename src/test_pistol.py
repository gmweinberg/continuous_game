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


if __name__ == '__main__':
    pistol_game = Game(score_pistol)
    strat1 = Strategy(0.4)
    strat2 = Strategy({0:0.9, 0.1:0.05, 0.399:0.05})
    print(pistol_game.resolve(strat1, strat2))
    print('hello')



