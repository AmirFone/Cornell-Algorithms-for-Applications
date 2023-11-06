from collections import defaultdict, deque
import itertools

# Function to create a node with a unique number
def create_node():
    create_node.num += 1
    return create_node.num

create_node.num = -1

# Function to add an edge to the graph
def add_edge(u, v, cap, bi):
    edges.append((u, v, cap, len(g[v])))
    g[u].append(len(edges) - 1)
    edges.append((v, u, bi, len(g[u])))
    g[v].append(len(edges) - 1)

# Function for the Dinic's algorithm
def dinic(u, min_edge):
    global it
    if u == dst:
        return min_edge
    for i in range(it[u], len(g[u])):
        e_idx = g[u][i]
        e = edges[e_idx]
        if level[u] + 1 == level[e[1]] and e[2] - f[e_idx] > 0:
            flow = dinic(e[1], min(min_edge, e[2] - f[e_idx]))
            if flow > 0:
                f[e_idx] += flow
                f[e_idx ^ 1] -= flow
                return flow
        it[u] += 1
    return 0

# Function for Breadth-First Search (BFS)
def bfs():
    global level
    q = deque()
    q.append(src)
    level = [0 for _ in range(nodes)]
    level[src] = 1
    while q:
        v = q.popleft()
        for i in range(len(g[v])):
            e_idx = g[v][i]
            e = edges[e_idx]
            if not level[e[1]] and e[2] - f[e_idx] > 0:
                q.append(e[1])
                level[e[1]] = level[v] + 1
    return level[dst]

# Main function for the card game
def cards_game(m, n, k, counts):
    global src, dst, f, g, edges, level, it, nodes
    src = create_node()
    dst = create_node()

    nodes = 2 * m * k + 2

    cards = defaultdict(int)
    f = [0] * nodes * (nodes + 1)
    g = defaultdict(list)
    edges = []
    level = [-1] * nodes
    it = 0

    # Count the number of each card in the counts
    for person in counts:
        for card in counts[person]:
            cards[card[0], card[1]] += 1

    # Create edges in the graph based on the counts
    for i, d in itertools.product(range(1, m + 1), range(1, k + 1)):
        node = 2 * ((i - 1) * k + d - 1)
        full_count = cards[(i, d)] // n
        add_edge(src, node, full_count, 0)
        add_edge(node, node + 1, cards[(i, d)], 0)
        if i < m:
            add_edge(node + 1, dst, full_count, 0) 
            add_edge(node + 1, 2 * (i * k + d - 1) + 2, cards[(i, d)] - full_count, 0) 

    # Create additional edges in the graph
    for i in range(1, m):
        for d in range(1, k + 1):
            add_edge(2 * ((i - 1) * k + d - 1) + 2, 2 * (i * k + d - 1) + 1, float('inf'), 0)

    res = 0
    # Use BFS and Dinic's algorithm to find the maximum flow
    while bfs():
        it = [0] * nodes
        while True:
            flow = dinic(src, float('inf'))
            if not flow:
                break
            res += flow
    return res
