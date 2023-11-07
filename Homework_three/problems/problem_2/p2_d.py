# import networkx as nx
# import matplotlib.pyplot as plt\
from collections import deque

# def visualize_res_graph(res_graph, n, k, source_idx=None, sink_idx=None, name='res_graph'):
#     plt.cla()
#     plt.clf()
#     G = nx.Graph()  # Create a directed graph object

#     if source_idx is None:
#         source_idx = n + k
#     if sink_idx is None:
#         sink_idx = n + k + 1

#     # Add nodes
#     for i in range(len(res_graph)):
#         G.add_node(i)

#     # Add edges based on rGraph adjacency lists
#     for i, neighbours in enumerate(res_graph):
#         for neighbor in neighbours:
#             G.add_edge(i, neighbor)

#     # Set position manually for nodes to ensure no overlaps
#     pos = {}
    
#     # Position nodes with label 'c'
#     for idx in range(n):
#         pos[idx] = (0.25, idx / (n-1))
    
#     # Position nodes with label 'r'
#     for idx in range(n, n+k):
#         pos[idx] = (0.75, (idx-n) / (k-1))

#     # Set position for the Source and Sink
#     pos[source_idx] = (0, 0.5)
#     pos[sink_idx] = (1, 0.5)

#     # Map nodes to labels
#     labels = {i: "prov" + str(i - n) if i >= n and i < n+k else "hub" + str(i) for i in range(n + k)}
#     labels[source_idx] = 'Source'
#     labels[sink_idx] = 'Sink'

#     # Draw the graph
#     nx.draw(G, pos, labels=labels, with_labels=True, node_color="skyblue", node_size=1000, font_size=10, font_weight='bold', edge_color='gray', width=2.0, alpha=0.6)
#     plt.savefig(name + ".png")


def ford_fulkerson(res_graph,source,sink):
    max_flow=0
    while True:
        path,path_flow = find_augmenting_path(res_graph, source, sink)
        if path is None:
            break
        max_flow+=path_flow
        update_residul_graph(res_graph, path, path_flow, source, sink)
    return max_flow


def find_augmenting_path(res_graph,source,sink):
    visited= [False]* len(res_graph)
    
    curr_path=[-1]*len(res_graph)
    
    queue= deque([source])
    
    visited[source]=True
    
    while queue:
        u = queue.popleft()
        for v in res_graph[u]:
            if not visited[v] and res_graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                curr_path[v]=u
                if v == sink:
                    path_flow = float('inf')
                    s = sink
                    while s != source:
                        path_flow = min(path_flow, res_graph[curr_path[s]][s])
                        s= curr_path[s]
                    return curr_path, path_flow
    return None, 0
def update_residul_graph(res_graph,path,path_flow,source,sink):
    if path is None:
        return 

    v = sink 
    while v != source:
        u = path[v]
        res_graph[u][v] -= path_flow
        res_graph[v][u] += path_flow
                        
        
def plan_city_d( 
    num_data_hubs,
    num_service_providers,
    connections, 
    provider_capacities, 
    preliminaryAssignment
):
    n = num_data_hubs
    k = num_service_providers
    source, sink = n + k, n + k + 1  

    # Create residual graph
    res_graph = [{} for _ in range(num_data_hubs + num_service_providers + 2)]
    
    for hub in range(n):
        res_graph[source][hub]=1
    
    for hub,providers in connections.items():
        for provider in providers:
            res_graph[hub][provider]=1
    
    for provider in range(n,n+k):
        res_graph[provider][sink] = provider_capacities[provider]
    
    for i in range(len(res_graph)):
        for j in res_graph[i]:
            if i not in res_graph[j]:
                res_graph[j][i]=0
    
    for hub, provider in preliminaryAssignment.items():
        res_graph[source][hub]-= 1 
        res_graph[hub][provider]-= 1 
        res_graph[provider][sink]-= 1 
        
        
        res_graph[sink][provider] += 1 
        res_graph[provider][hub] += 1 
    
    max_flow = ford_fulkerson(res_graph, source, sink)
    if max_flow == 1:
        return True
    else:
        return False