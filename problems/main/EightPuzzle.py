from problems.model.impl.EightPuzzleProblem import EigthPuzzleProblem
from search.model.impl.BreadthFirstSearch import BreadthFirstSearch
from search.model.impl.DepthFirstSearch import DepthFirstSearch
from search.model.impl.DepthFirstSearch import IterativeDeepingDFS
from search.model.impl.UniformedCostSearch import UniformedCostSearch
from search.model.impl.BidirectionalSearch import BidirectionalSearch
import numpy as np

board = np.array([2, 0, 6, 5, 1, 7, 3, 4, 8]).reshape(3, 3)

p = EigthPuzzleProblem(3, board)

s = BidirectionalSearch(p)
print(s.solve(), s.solution_cost)

s = IterativeDeepingDFS(p)
print(s.solve(), s.solution_cost)

s = DepthFirstSearch(p, 7)
print(s.solve(), s.solution_cost)

s = BreadthFirstSearch(p)
print(s.solve(), s.solution_cost)

s = UniformedCostSearch(p)
print(s.solve(), s.solution_cost)
