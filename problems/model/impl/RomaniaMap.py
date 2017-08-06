import matplotlib.pyplot as plt
import networkx as nx
from search.model.impl.BreadthFirstSearch import BreadthFirstSearch
from search.model.impl.DepthFirstSearch import DepthFirstSearch
from search.model.impl.DepthFirstSearch import IterativeDeepingDFS
from problems.model.impl.MapProblem import MapProblem

map_graph = dict(
    Arad=dict(
        Zerind=dict(distance=75),
        Sibiu=dict(distance=140),
        Timisoara=dict(distance=118)
    ),
    Bucharest=dict(
        Urziceni=dict(distance=85),
        Pitesti=dict(distance=101),
        Giurgiu=dict(distance=90),
        Fagaras=dict(distance=211)
    ),
    Craiova=dict(
        Drobeta=dict(distance=120),
        Rimnicu=dict(distance=146),
        Pitesti=dict(distance=138)
    ),
    Drobeta=dict(
        Mehadia=dict(distance=75)
    ),
    Eforie=dict(
        Hirsova=dict(distance=86)
    ),
    Fagaras=dict(
        Sibiu=dict(distance=99)
    ),
    Hirsova=dict(
        Urziceni=dict(distance=98)
    ),
    Iasi=dict(
        Vaslui=dict(distance=92),
        Neamt=dict(distance=87)
    ),
    Lugoj=dict(
        Timisoara=dict(distance=111),
        Mehadia=dict(distance=70)
    ),
    Oradea=dict(
        Zerind=dict(distance=71),
        Sibiu=dict(distance=51)
    ),
    Pitesti=dict(
        Rimnicu=dict(distance=97)
    ),
    Rimnicu=dict(
        Sibiu=dict(distance=80)
    ),
    Urziceni=dict(
        Vaslui=dict(distance=142)
    )
)

locations_positions = dict(
    Arad=(91, 492),
    Bucharest=(400, 327),
    Craiova=(253, 288),
    Drobeta=(165, 299),
    Eforie=(562, 293),
    Fagaras=(305, 449),
    Giurgiu=(375, 270),
    Hirsova=(534, 350),
    Iasi=(473, 506),
    Lugoj=(165, 379),
    Mehadia=(168, 339),
    Neamt=(406, 537),
    Oradea=(131, 571),
    Pitesti=(320, 368),
    Rimnicu=(233, 410),
    Sibiu=(207, 457),
    Timisoara=(94, 410),
    Urziceni=(456, 350),
    Vaslui=(509, 444),
    Zerind=(108, 531)
)

p = MapProblem(map_graph, locations_positions, "Arad", "Bucharest")

bfs = IterativeDeepingDFS(p, True)
actions = bfs.solve()

print(actions)
p.show_map()
