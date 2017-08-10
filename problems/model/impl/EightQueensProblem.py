import random as random
import math
import numpy as np
from problems.model.Problem import Problem
from search.model.Heuristic import Heuristic


class EigthQueensProblem(Problem):

    def __init__(self, number_of_queens=8, initial=None):
        self.queens = number_of_queens
        if initial is None:
            i = 1
            initial = []
            while i <= self.queens:
                initial.append(random.randint(1, self.queens-1))
                i += 1
        Problem.__init__(self, initial, None)

    def actions(self, state):
        c = 0
        actions = []
        while c < self.queens:
            r = 1
            while r <= self.queens:
                if not (state[c] == r):
                    tmp = np.array(state)
                    tmp[c] = r
                    actions.append(tmp)
                r += 1
            c += 1
        return actions

    def result(self, state, action):
        return np.copy(action)

    def goal_test(self, state):
        c = 0
        while c < state.__len__():
            r = c + 1
            while r < state.__len__():
                offset = math.fabs(r - c)
                same_row = state[r] == state[c]
                up_diagonal = state[r] == (state[c] - offset)
                dw_diagonal = state[r] == (state[c] + offset)
                if same_row or up_diagonal or dw_diagonal:
                    return False
                r += 1
            c += 1
        return True

    @staticmethod
    def same_state(state1, state2):
        return np.array_equal(state1, state2)

    def print_board(self, state):
        board = np.chararray((self.queens, self.queens), itemsize=3, unicode=True)
        board[:] = "-"
        i = 0
        for item in state:
            board[item-1][i] = "Q"
            i += 1
        print(board)


class EightQueensHeuristic(Heuristic):
    def __init__(self):
        Heuristic.__init__(self, None)

    def get_heuristic_cost(self, state):
        """ Simply return, for a state, the number of queen's pairs that attack eachother directly or indirectly"""
        res = 0
        c = 0
        while c < state.__len__():
            r = c+1
            while r < state.__len__():
                offset = math.fabs(r - c)
                same_row = state[r] == state[c]
                up_diagonal = state[r] == (state[c] - offset)
                dw_diagonal = state[r] == (state[c] + offset)
                if same_row or up_diagonal or dw_diagonal:
                    res += 1
                r += 1
            c += 1
        return res
