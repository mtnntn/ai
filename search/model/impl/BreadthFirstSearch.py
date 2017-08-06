from problems.model.impl.EightPuzzleProblem import EigthPuzzleProblem
from search.model.Search import Search


class BreadthFirstSearch(Search):

    def __init__(self, prob, trace=False):
        Search.__init__(self, prob, trace)

    def solve(self):
        while list.__len__(self.frontier) > 0:

            if self.trace:
                print("\nFrontier :")
                for el in self.frontier:
                    print("\n")
                    print(el)
                print("\nExplored Set:")
                for el in self.exploredset:
                    print("\n")
                    print(el)

            currentnode = self.frontier.pop(0)
            self.exploredset.append(currentnode.state)

            if self.problem.goal_test(currentnode.state):
                return self.solution(currentnode)

            if self.trace:
                print("_____________________________________________________________________________")
                print("\n\nExpansion of\n")
                print(currentnode)

            for action in self.problem.actions(currentnode.state):
                child = self.child_node(currentnode, action)

                if self.trace:
                    print("-------------------------------------------------------------")
                    print(child)

                if not self.already_explored(child.state):
                    if self.trace:
                        print("\n State not explored yet:")
                    if not self.already_in_frontier(child.state):
                        if self.trace:
                            print("\n Node is not in frontier")
                        if self.problem.goal_test(child.state):
                            if self.trace:
                                print("\n This state is a solution! \n")
                            return self.solution(child)
                        if self.trace:
                            print("\n Add it to the frontier")
                        self.frontier.append(child)
                if self.trace:
                    print("------------------------------------------------------------")
            if self.trace:
                print("_____________________________________________________________________________")

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

