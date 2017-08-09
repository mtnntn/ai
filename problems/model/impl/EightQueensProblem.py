import random as random
import numpy as np
from problems.model.Problem import Problem


class EigthPuzzleProblem(Problem):

    def __init__(self, number_of_queens=8, initial=None):
        self.queens = number_of_queens
        if initial is None:
            i = 0
            initial = []
            while i < self.queens:
                initial.append(random.randint(0, self.queens-1))
                i += 1
        Problem.__init__(self, initial, None)

    def actions(self, state):
        c = 0
        actions = []
        while c < self.queens:
            r = 0
            while r < self.queens:
                if not r == state[c]:
                    tmp = np.array(state)
                    tmp[c] = r
                    actions.append(tmp)
                r += 1
            c += 1
        return actions

    def result(self, state, action):
        return np.copy(action)

    def goal_test(self, state):
        res = True
        c = 0
        while c < self.queens and res:
            r = 0
            while r < self.queens and res:
                if not r == c:
                    # I must check if the queen on column r attack diagonally the queen on column c
                    # interested position is in position |c-r|
                    if c < r:
                        res = not (state[r] == c-r)
                    elif c > r:
                        res = not (state[r] == r-c)
                    else:
                        # break if we have on the same row 2 queens
                        res = not (state[c] == state[r])
                r += 1
            c += 1
        return res

    @staticmethod
    def same_state(state1, state2):
        return np.array_equal(state1, state2)

    def print_board(self, state):
        board = np.chararray((self.queens, self.queens), itemsize=3, unicode=True)
        board[:] = ":"
        i = 0
        for item in state:
            board[item][i] = "Q"
            i += 1
        print(board)
