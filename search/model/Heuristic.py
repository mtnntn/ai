class Heuristic(object):

    def __init__(self, table):
        self.table = table

    def get_heuristic_cost(self, state):
        return self.table[state]
