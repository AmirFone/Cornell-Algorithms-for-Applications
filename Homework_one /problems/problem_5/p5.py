'''
Problem 5

input: List of tuples representing the friend's apartments.
output: List of apartment pairs.

TODO: implement your solution.
'''
def cookies_distrubution_map(flat_bldgs) -> list:
    import copy
    import heapq
    def calc_manhattan_dist(node1,node2): return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    def construct_graph(flat_bldgs):
        flat_bldgs.insert(0,(1,1))
        graph = {}
        for i in range(len(flat_bldgs)):
            graph[i] = []

        for i in range(len(flat_bldgs)):
            for j in range(i+1, len(flat_bldgs)):
                x = flat_bldgs[i]
                y = flat_bldgs[j]
                weight = calc_manhattan_dist(x,y)
                graph[i].append((weight,i,j))
                graph[j].append((weight,j,i ))
        
        return graph
    
    bldgs_graph = construct_graph(flat_bldgs)
    print(bldgs_graph)
    visited = set()
    heap = copy.copy(bldgs_graph[0])
    heapq.heapify(heap)
    visited.add(0)
    MST = []
    result = []
    print(heap)
    while len(visited) < len(flat_bldgs):
        weight, start, node = heapq.heappop(heap)
        if node not in visited:
            MST.append((start, node, weight))
            for neighbor in bldgs_graph[node]:
                weight, s, nx = neighbor
                if nx not in visited:
                    heapq.heappush(heap, neighbor)
            visited.add(node)
    print(MST)
    for i in MST:
        start, end, _ = i
        result.append((flat_bldgs[start], flat_bldgs[end]))
    return result