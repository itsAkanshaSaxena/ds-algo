from collections import defaultdict


class Graph:
    def __init__(
        self,
    ):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited):
        visited.add(v)

        for node in self.graph[v]:
            if node not in visited:
                self.dfs(node, visited)

    def init_dfs(self, v):
        visited = set()

        self.dfs(v, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.init_dfs(2)

print(g.graph)
