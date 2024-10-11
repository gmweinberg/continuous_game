#!/usr/bin/env python

"""A Game here is a two-player game for which each player has a continuous range of possible actions.
   The game attributes of the game are the range of actions for each player and a score function.
"""

class Game:
    def __init__(self, score, range1=None, range2=None):
        self.score = score
        if range1 is None:
            self.range1 = (0, 1)
        else:
            self.range1 = range1

        if range2 is None:
            self.range2 = (0, 1)
        else:
            self.range2 = range2

    def simulate(self, strat1, start2, rounds=10000):
        """Simulate the interaction of two strategies. This is only worthwhile if the strategies are
           continuous functions."""

        scores = [0.0, 0.0]
        for ii in range(rounds):
            ascore = self.score(strat1.sample(), strat2.sample())
            scores[0] += ascore[0]
            scores[1] += ascore[1]
        scores /= rounds
        return scores

    def resolve(self, strat1, strat2):
        """Determine how strat1 vs strat2 scores. This only works if both startegies are discrete."""
        if not (strat1.discrete and strat2.discrete):
            raise Exception("Both strategies must be discrete")
        scores = [0.0, 0.0]
        for elm1 in strat1.dist:
            for elm2 in strat2.dist:
                prod = strat1.dist[elm1] * strat2.dist[elm2]
                ascores = self.score(elm1, elm2)
                scores[0] += prod * ascores[0]
                scores[1] += prod * ascores[1]
        return scores



