import math

from search.model.Node import Node
from search.model.Search import Search


class DepthFirstSearch(Search):

    def __init__(self, problem, limit=math.inf, trace=False):
        self.limit = limit
        Search.__init__(self, problem, trace)

    def solve(self):
        initialnode = Node(self.problem.initial_state)
        return self.recursive_limited_dsf(initialnode, self.limit)

    def recursive_limited_dsf(self, node, limit):
        if self.trace:
            print("Currently in ", node, "and limit: ", limit)
        if self.problem.goal_test(node.state):
            if self.trace:
                print("Solution find")
            return self.solution(node)
        elif limit is 0:
            if self.trace:
                print("limit is 0==", limit, " -> cutoff")
            return "cutoff"
        else:
            cutoff_occurred = False
            for action in self.problem.actions(node.state):
                child = self.child_node(node, action)
                if self.trace:
                    print("recursive call on ", child)
                res = self.recursive_limited_dsf(child, limit-1)
                if isinstance(res, str) and res.__eq__("cutoff"):
                    cutoff_occurred = True
                elif res is not None:
                    return res
            return "cutoff" if cutoff_occurred else None


class IterativeDeepingDFS(DepthFirstSearch):

    def __init__(self, problem, trace=False):
        Search.__init__(self, problem, trace)

    def solve(self):
        self.limit = 0
        while self.limit < math.inf:
            initialnode = Node(self.problem.initial_state)
            res = self.recursive_limited_dsf(initialnode, self.limit)
            if isinstance(res, str) and res.__eq__("cutoff"):
                self.limit += 1
            else:
                return res
