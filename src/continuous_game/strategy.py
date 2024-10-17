#!/usr/bin/env python

from random import random

class Strategy:
    """A strategy represents the probabilities of playing various actions. It
    can be a discrete set of probabilities (which must be nonnegative and must sum to one)
    or a continuous function over some range (which must be nonnegative and integrate to one)."""

    def __init__(self, dist=None, fun=None):
        if fun is None and dist is None:
            raise Exception("Must supply fun or dist""")
        if dist is not None:
            if type(dist) == type({}):
                self.dist = dist
            else:
                self.dist = {dist:1} # constant
            self.discrete = True
        else:
            self.fun = fun
            self.discrete = False

    def sample(self):
        if self.discrete:
            sam = random()
            for elm in self.dist:
                prob = self.dist[elm]
                if sam <= prob:
                    return elm
                sam -= prob
        else:
            return self.fun(random())

    def validate(self):
        if self.discrete:
            total = sum([self.dist[elm] for elm in self.dist])
            if abs(total) > 1e-8:
                raise Exception("Invalid distribution")
            return True
        raise Exception("Not implemented")

    def normalize(self):
        if self.discrete:
            total = sum([self.dist[elm] for elm in self.dist])
            new_dist = {elm: self.dist[elm] / total for elm in self.dist}
            if abs(total) > 1e-8:
                raise Exception("Invalid distribution")
            return True
        raise Exception("Not implemented")


