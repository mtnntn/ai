from problems.model.Problem import Problem
import networkx as nx
import matplotlib.pyplot as plt


class MapProblem(Problem):

    def __init__(self, mapgraph, positions, start, destination):
        self.nxgraph = nx.Graph(mapgraph)
        self.locations_positions = positions
        self.initial_state = start
        self.destination = destination
        Problem.__init__(self, self.initial_state, self.destination)

    def actions(self, state):
        if self.nxgraph.has_node(state):
            return list(self.nxgraph[state].keys())
        return None

    def result(self, state, action):
        if self.nxgraph.has_node(state):
            state = self.nxgraph[state]
            if state.get(action) is not None:
                return action
        return None

    def goal_test(self, state):
        return self.same_state(self.goal_state, state)

    def step_cost(self, c, state1=None, action=None, state2=None):
        return c + self.nxgraph[state1][action]["distance"]

    @staticmethod
    def same_state(state1, state2):
        return state1.__eq__(state2)

    def show_map(self, nodecolors=None):
        node_labels = dict()
        node_colors = dict()
        edge_labels = dict()
        for n1 in self.nxgraph.nodes():
            node_labels[n1] = n1

            if nodecolors is None:
                node_colors[n1] = "white"
            else:
                node_colors[n1] = nodecolors[n1]

            for n2 in self.nxgraph[n1]:
                edge_labels[(n1, n2)] = self.nxgraph[n1][n2]["distance"]

        node_label_pos = {cityname: [position[0], position[1] - 10] for cityname, position in
                          self.locations_positions.items()}

        plt.figure(figsize=(18, 23))
        nx.draw(self.nxgraph, pos=self.locations_positions, node_color=[node_colors[nd] for nd in self.nxgraph.nodes()])
        nx.draw_networkx_labels(self.nxgraph, pos=node_label_pos, labels=node_labels, font_size=14)
        nx.draw_networkx_edge_labels(self.nxgraph, pos=self.locations_positions, edge_labels=edge_labels, font_size=14)
        plt.show()
