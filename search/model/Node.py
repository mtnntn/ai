import numpy as np


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
