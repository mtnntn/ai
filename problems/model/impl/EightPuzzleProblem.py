from problems.model.Problem import Problem
from random import shuffle
import numpy as np


class EigthPuzzleProblem(Problem):

    def __init__(self, board_size=3, initial=None):
        self.possible_actions = ["UP", "DW", "SX", "DX"]
        self.boardSize = board_size
        ls = list(range(self.boardSize * self.boardSize))
        goal = np.array(ls, int).reshape(self.boardSize, self.boardSize)
        if initial is None:
            shuffle(ls)
            initial = np.array(ls, int).reshape(self.boardSize, self.boardSize)
        Problem.__init__(self, initial, goal)

    def actions(self, state):
        acts = list(self.possible_actions)
        zeroix = np.where(state == 0)
        rowzero = zeroix[0][0]
        colzero = zeroix[1][0]
        if rowzero == 0:
            acts.remove("UP")
        if rowzero == self.boardSize-1:
            acts.remove("DW")
        if colzero == 0:
            acts.remove("SX")
        if colzero == self.boardSize-1:
            acts.remove("DX")
        return acts

    def result(self, state, action):
        zeroix = np.where(state == 0)
        rowzero = zeroix[0][0]
        colzero = zeroix[1][0]
        newstate = np.copy(state)
        if action == "UP":
            if action in self.actions(state):
                newstate[rowzero][colzero] = newstate[rowzero-1][colzero]
                newstate[rowzero - 1][colzero] = 0
            else:
                raise BaseException("Is not possible to execute given action in current state!")
            return newstate
        elif action == "DW":
            if action in self.actions(state):
                newstate[rowzero][colzero] = newstate[rowzero+1][colzero]
                newstate[rowzero + 1][colzero] = 0
            else:
                raise BaseException("Is not possible to execute given action in current state!")
            return newstate
        elif action == "SX":
            if action in self.actions(state):
                newstate[rowzero][colzero] = newstate[rowzero][colzero-1]
                newstate[rowzero][colzero - 1] = 0
            else:
                raise BaseException("Is not possible to execute given action in current state!")
            return newstate
        elif action == "DX":
            if action in self.actions(state):
                newstate[rowzero][colzero] = newstate[rowzero][colzero+1]
                newstate[rowzero][colzero + 1] = 0
            else:
                raise BaseException("Is not possible to execute given action in current state!")
            return newstate
        else:
            raise BaseException("Action %s specified is unknown!" % action)

    def goal_test(self, state):
        return self.same_state(self.goal_state, state)

    @staticmethod
    def same_state(state1, state2):
        return np.array_equal(state1, state2)
