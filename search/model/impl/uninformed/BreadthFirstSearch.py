from search.model.Search import Search


class BreadthFirstSearch(Search):

    def __init__(self, prob):
        Search.__init__(self, prob)

    def solve(self):

        while list.__len__(self.frontier) > 0:

            currentnode = self.frontier.pop(0)
            self.exploredset.append(currentnode.state)

            if self.problem.goal_test(currentnode.state):
                return self.solution(currentnode)

            for action in self.problem.actions(currentnode.state):
                child = self.child_node(currentnode, action)

                if not self.already_explored(child.state):
                    if not self.already_in_frontier(child.state):
                        if self.problem.goal_test(child.state):
                            return self.solution(child)
                        self.frontier.append(child)

    def already_explored(self, state):
        for st in self.exploredset:
            if self.problem.same_state(st, state):
                return True
        return False

    def already_in_frontier(self, state):
        for st in self.frontier:
            if self.problem.same_state(st.state, state):
                return True
        return False
