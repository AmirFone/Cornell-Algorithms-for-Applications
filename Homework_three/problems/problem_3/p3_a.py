from collections import defaultdict

# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u-1][v-1] = 1
        self.graph[v-1][u-1] = 1
        
    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False

    # Returns tne maximum flow from s to t in the given graph
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0  # There is no flow initially

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def find_paths(n, paths):
    g = Graph(n)
    for u, v in paths:
        g.add_edge(u, v)

    source = 0  # Masters Studio
    sink = n - 1  # Tata Innovation Center

    return g.ford_fulkerson(source, sink)
