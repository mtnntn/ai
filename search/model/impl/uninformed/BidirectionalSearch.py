from search.model.Node import Node
from search.model.Search import Search


class BidirectionalSearch(Search):

    def __init__(self, problem):

        if isinstance(problem.goal_state, list):
            self.back_initial_state = problem.goal_state[0]
        else:
            self.back_initial_state = problem.goal_state

        self.back_goal_state = problem.initial_state

        self.back_exploredset = []
        self.back_frontier = [Node(self.back_initial_state)]

        Search.__init__(self, problem)

    def solve(self):

        while list.__len__(self.frontier) > 0 or list.__len__(self.back_frontier) > 0:

            currentnode = self.frontier.pop(0)
            self.exploredset.append(currentnode.state)

            currentnode_back = self.back_frontier.pop(0)
            self.back_exploredset.append(currentnode_back.state)

            if self.problem.goal_test(currentnode.state):
                return self.solution(currentnode)
            elif self.problem.same_state(self.back_goal_state, currentnode_back.state):
                return self.solution(currentnode_back).reverse()
            elif self.problem.same_state(currentnode.state, currentnode_back.state):
                l1 = self.solution(currentnode)
                l2 = self.solution(currentnode_back).reverse()
                if l2 is not None:
                    l2.pop()
                return list.append(l1, l2)
            res = self.new_expansion(self.problem, currentnode, self.exploredset, self.frontier)
            if res is None:
                res = self.new_expansion(self.problem, currentnode_back, self.back_exploredset, self.back_frontier)
                if res is not None:
                    return res.reverse()
            else:
                return res

    def new_expansion(self, problem, currentnode, exploredset, frontier):
        for action in problem.actions(currentnode.state):
            child = self.child_node(currentnode, action)

            if not self.already_explored(child.state, problem, exploredset):
                if not self.already_in_frontier(child.state, problem, frontier):
                    if problem.goal_test(child.state):
                        return self.solution(child)
                    frontier.append(child)

    @staticmethod
    def already_explored(state, problem, exploredset):
        for st in exploredset:
            if problem.same_state(st, state):
                return True
        return False

    @staticmethod
    def already_in_frontier(state, problem, frontier):
        for st in frontier:
            if problem.same_state(st.state, state):
                return True
        return False
