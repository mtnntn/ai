import numpy as np
from problems.model.impl.EightPuzzleProblem import EigthPuzzleProblem
from problems.model.impl.EightPuzzleProblem import EightPuzzleHeuristic
from search.model.impl.uninformed.BidirectionalSearch import BidirectionalSearch
from search.model.impl.uninformed.BreadthFirstSearch import BreadthFirstSearch
from search.model.impl.uninformed.UniformCostSearch import UniformCostSearch
from search.model.impl.uninformed.DepthFirstSearch import DepthFirstSearch
from search.model.impl.uninformed.DepthFirstSearch import IterativeDeepingDFS
from search.model.impl.informed.AStarSearch import AStarSearch
from search.model.impl.informed.GreedySearch import GreedySearch
from search.model.Heuristic import Heuristic

# board = np.array([2, 0, 6, 5, 1, 7, 3, 4, 8]).reshape(3, 3)
# board = np.array([7, 2, 4, 5, 0, 6, 8, 3, 1]).reshape(3, 3)
board = np.array([2, 8, 3, 1, 6, 4, 7, 0, 5]).reshape(3, 3)
finalboard = np.array([1, 2, 3, 8, 0, 4, 7, 6, 5]).reshape(3, 3)

p = EigthPuzzleProblem(3, board)
p.goal_state = finalboard

heur = EightPuzzleHeuristic()

# All this line are commented because is very inefficient run an uninformed search strategy for the 8 Puzzle problem.

# s = BidirectionalSearch(p)
# print(s.solve(), s.solution_cost)
# s = IterativeDeepingDFS(p)
# print(s.solve(), s.solution_cost)
# s = DepthFirstSearch(p, 7)
# print(s.solve(), s.solution_cost)
# s = BreadthFirstSearch(p)
# print(s.solve(), s.solution_cost)
# s = UniformCostSearch(p)
# print(s.solve(), s.solution_cost)

# s = GreedySearch(p, heur)
# print(s.solve(), s.solution_cost)

s = AStarSearch(p, heur)
print(s.solve(), s.solution_cost)
