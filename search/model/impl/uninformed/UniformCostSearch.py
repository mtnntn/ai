from search.model.Search import Search
from search.model.Node import Node
from bisect import insort_left


class UniformCostSearch(Search):

    def __init__(self, problem, trace=False):
        Search.__init__(self, problem, trace)
        self.frontier = sorted([Node(self.problem.initial_state)])

    def solve(self):

        while list.__len__(self.frontier) > 0:
            currnode = self.frontier.pop(0)

            if self.problem.goal_test(currnode.state):
                return self.solution(currnode)

            self.exploredset.append(currnode.state)

            for action in self.problem.actions(currnode.state):
                child = self.child_node(currnode, action)
                explored = self.already_explored(child.state)
                in_frontier = self.already_in_frontier(child)

                if not explored and in_frontier is -1:
                    insort_left(self.frontier, child)
                elif in_frontier is not -1:
                    old = self.frontier.pop(in_frontier)

                    if old.path_cost > child.path_cost:
                        self.frontier.insert(in_frontier, child)
                    else:
                        self.frontier.insert(in_frontier, old)

    def already_explored(self, state):
        for st in self.exploredset:
            if self.problem.same_state(st, state):
                return True
        return False

    def already_in_frontier(self, child):
        res = 0
        for st in self.frontier:
            if self.problem.same_state(st.state, child.state):
                return res
            res += 1
        return -1
