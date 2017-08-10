from search.model.impl.local.HillClimbingSearch import HillClimbing
from problems.model.impl.EightQueensProblem import EigthQueensProblem
from problems.model.impl.EightQueensProblem import EightQueensHeuristic

p = EigthQueensProblem()
h = EightQueensHeuristic()

s = HillClimbing(p, h, 100)

print(s.solve())

