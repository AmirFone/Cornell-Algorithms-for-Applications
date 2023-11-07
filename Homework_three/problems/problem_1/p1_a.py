# Problem 1a
from collections import deque, defaultdict
def is_bipartite(g):
    # print(g)
    # print(g[0])
    color = {}
    for node in g:
        if node not in color:
            queue = deque([node])
            color[node] = 0
            while queue:
                node = queue.popleft()
                for neighbor in g[node]:
                    if neighbor not in color:
                        color[neighbor] = color[node] ^ 1
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
    # print(color)
    return True
