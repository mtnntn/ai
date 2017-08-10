from search.model.Search import Search
from search.model.Node import HeuristicNode
from bisect import insort_left


class HillClimbing(Search):

    """ HillClimbing search is the simplest type of local search. This Alghoritm just iterate over and over trying
    to maximize the value of an heuristic/objective function in order to get better results. Different version of this
    alghoritm depends on what it decides to do when no better moves are avaiable in the current state.
    In this version I have implemented a version where the alghoritm continue it's execution when no beter moves are
    avaiable doing at max 100 'sideway moves'. The constructor, owever, allow to specify different values.

    The frontier mantains a map of 'neighbors' for the current state.
    This map has 3 values UP, LW and EQ each one contains a list of nodes that have respectively an higher,
    lower or equal value of the cost value."""

    def __init__(self, problem, heuristic, max_sideway_moves=100):
        Search.__init__(self, problem)
        self.heuristic = heuristic
        self.max_sideway_moves = max_sideway_moves

    def solve(self):

        currnode = HeuristicNode(self.problem.initial_state)
        currnode.total_cost = currnode.heuristic_cost = self.heuristic.get_heuristic_cost(self.problem.initial_state)
        best_node = currnode
        keep_going = True
        while keep_going:
            self.improve(currnode)
            up = self.frontier.get("better")
            eq = self.frontier.get("equal")
            lw = self.frontier.get("worst")
            if up.__len__() > 0:
                currnode = up.pop(0)
                if best_node.total_cost > currnode.total_cost:
                    best_node = currnode
            elif eq.__len__() > 0 and not self.max_sideway_moves == 0:
                self.max_sideway_moves -= 1
                currnode = eq.pop()
            elif lw.__len__() > 0 and not self.max_sideway_moves == 0:
                self.max_sideway_moves -= 1
                currnode = lw.pop()
            keep_going = not (self.max_sideway_moves == 0 or best_node.heuristic_cost == 0)

        return best_node.state

    def improve(self, currnode):
        self.frontier = dict(
            better=sorted([]),
            equal=sorted([]),
            worst=sorted([]),
        )
        actions = self.problem.actions(currnode.state)
        for action in actions:
            child = self.child_node(currnode, action)
            if child.total_cost < currnode.total_cost:
                insort_left(self.frontier.get("better"), child)
            elif child.total_cost == currnode.total_cost:
                insort_left(self.frontier.get("equal"), child)
            else:
                insort_left(self.frontier.get("worst"), child)

    def solution(self, node):
        """ Return the solution of the problem, in this kind of alghoritms the solution is simply the state of the
        best node found. """
        self.solution_cost = node.heuristic_cost
        return node.state

    def child_node(self, parent, action):
        state = self.problem.result(parent.state, action)
        heuristic_cost = self.heuristic.get_heuristic_cost(state)
        n = HeuristicNode(state, None, None, 0, heuristic_cost)
        return n
