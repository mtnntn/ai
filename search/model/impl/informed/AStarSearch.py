from search.model.Search import Search
from search.model.Node import HeuristicNode
from bisect import insort_left


class AStarSearch(Search):

    def __init__(self, problem, heuristic):
        Search.__init__(self, problem)
        self.heuristic = heuristic
        self.frontier = sorted([HeuristicNode(self.problem.initial_state)])

    def solve(self):

        while list.__len__(self.frontier) > 0:

            currnode = self.frontier.pop(0)

            self.exploredset.append(currnode.state)

            if self.problem.goal_test(currnode.state):
                return self.solution(currnode)

            for action in self.problem.actions(currnode.state):
                child = self.child_node(currnode, action)
                explored = self.already_explored(child.state)
                in_frontier = self.already_in_frontier(child)

                if not explored and in_frontier is -1:
                    insort_left(self.frontier, child)
                elif in_frontier is not -1:
                    old = self.frontier.pop(in_frontier)

                    if old.total_cost > child.total_cost:
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

    def child_node(self, parent, action):
        state = self.problem.result(parent.state, action)
        heuristic_cost = self.heuristic.get_heuristic_cost(state)
        path_cost = self.problem.step_cost(parent.path_cost, parent.state, action, state)
        n = HeuristicNode(state, parent, action, path_cost, heuristic_cost, parent.level+1)
        return n
