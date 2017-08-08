import numpy as np
from problems.model.impl.EightPuzzleProblem import EigthPuzzleProblem
from search.model.impl.uninformed.BidirectionalSearch import BidirectionalSearch
from search.model.impl.uninformed.BreadthFirstSearch import BreadthFirstSearch
from search.model.impl.uninformed.UniformCostSearch import UniformCostSearch
from search.model.impl.uninformed.DepthFirstSearch import DepthFirstSearch
from search.model.impl.uninformed.DepthFirstSearch import IterativeDeepingDFS

# board = np.array([2, 0, 6, 5, 1, 7, 3, 4, 8]).reshape(3, 3)
board = np.array([7, 2, 4, 5, 0, 6, 8, 3, 1]).reshape(3, 3)

p = EigthPuzzleProblem(3, board)

s = BidirectionalSearch(p)
print(s.solve(), s.solution_cost)

s = IterativeDeepingDFS(p)
print(s.solve(), s.solution_cost)

s = DepthFirstSearch(p, 7)
print(s.solve(), s.solution_cost)

s = BreadthFirstSearch(p)
print(s.solve(), s.solution_cost)

s = UniformCostSearch(p)
print(s.solve(), s.solution_cost)
