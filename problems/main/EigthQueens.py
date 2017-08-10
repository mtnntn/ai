from search.model.impl.local.HillClimbingSearch import HillClimbing
from search.model.impl.local.HillClimbingSearch import StochasticHillClimber
from problems.model.impl.EightQueensProblem import EigthQueensProblem
from problems.model.impl.EightQueensProblem import EightQueensHeuristic

p = EigthQueensProblem()
h = EightQueensHeuristic()

# s = HillClimbing(p, h, 100)
# sol = s.solve()
# print(sol, print(p.goal_test(sol)))

p = EigthQueensProblem(10)
s = StochasticHillClimber(p, h, 100000000, 2000)
sol = s.solve()

print(sol, "\n", p.goal_test(sol), "\n")
p.print_board(sol)

