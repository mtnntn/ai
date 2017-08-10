class Node(object):
    """ Search algorithms require a data structure to keep track of the search tree that is being constructed.
    For each node n of the tree, we have a structure that contains four components:
    -STATE     : the state in the state space to which the node corresponds;
    -PARENT    : the node in the search tree that generated this node;
    -ACTION    : the action that was applied to the parent to generate the node;
    -PATH_COST : the cost of the path from the initial stateto the node, as indicated by the parent pointers."""

    def __init__(self, state=None, parent=None, action=None, path_cost=0, level=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.level = level

    def __repr__(self):
        return " %s  action: %s , cost: %d , level: %d" % (self.state, self.action, self.path_cost, self.level)

    def __lt__(self, other):
        return self.path_cost < other.path_cost


class HeuristicNode(Node):
    def __init__(self, state=None, parent=None, action=None, path_cost=0, heuristic_cost=0, level=0):
        Node.__init__(self, state, parent, action, path_cost, level)
        self.heuristic_cost = heuristic_cost
        self.total_cost = heuristic_cost + path_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def __repr__(self):
        return " %s  action: %s , path_cost: %d , heur_cost: %d , tot_cost: %d , level: %d" % (self.state, self.action,
                                                                                               self.path_cost,
                                                                                               self.heuristic_cost,
                                                                                               self.total_cost,
                                                                                               self.level)


class GameNode(object):

    def __init__(self, state=None, parent=None, action=None, utility=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.utility = utility

    def __lt__(self, other):
        return self.utility < other.utility

    def __gt__(self, other):
        return self.utility > other.utility

    def __repr__(self):
        return " %s  - action: %s, utility: %d" % (self.state, self.action, self.utility)
