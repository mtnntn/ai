from search.model.Node import Node


class Search(object):
    """ An Abstract Search Object take as input a problem
    A concrete implementation must redefine it's own solve method.
    """

    def __init__(self, problem, trace=False):
        """ Set the problem to solve, initialize the explored set with a new list and the frontier with the initial
        state of the problem to solve. """
        self.trace = trace
        self.problem = problem
        self.pathcost = 0
        self.exploredset = []
        self.frontier = [Node(problem.initial_state)]
        self.solution_cost = 0

    def get_solution_nodes(self, node):
        """ Return a list of node rebuilded thanks to the parent pointer.
        The list represent the list of nodes to be attraversed in order to solve the problem. """
        result = list()
        self.solution_cost = node.path_cost
        while node is not None:
            result.append(node)
            node = node.parent
        return result

    def solution(self, node):
        """ Return a list of actions to be executed in order to solve the problem. The list represent the solution
        for the problem and is build back thanks to the parent's pointer of each node. """
        result = list()
        self.solution_cost = node.path_cost
        while node.action is not None:
            result.insert(0, node.action)
            node = node.parent
        return result

    def child_node(self, parent, action):
        """ Given a parent node and an action this method allow to initialize a new node for the problem wich is the"""
        state = self.problem.result(parent.state, action)
        pathcost = self.problem.step_cost(parent.path_cost, parent.state, action, state)
        n = Node(state, parent, action, pathcost, parent.level+1)
        return n

    def solve(self):
        """ Each Class that extend the Search class must implement this metod that allow to generate a solution.
        This allow to define a class for each different alghorithm of Search that implements only it's own strategy
        to solve the problem. """
        raise NotImplementedError
