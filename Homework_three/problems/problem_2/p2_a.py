# Problem 2a,b,c 
# NOTE: Problem B and C are to be implemented in this file as well

import networkx as nx
import matplotlib.pyplot as plt


def visualize_res_graph(res_graph, n, k, source_idx=None, sink_idx=None, name='res_graph'):
    plt.cla()
    plt.clf()
    G = nx.DiGraph()  # Create a directed graph object

    if source_idx is None:
        source_idx = n + k
    if sink_idx is None:
        sink_idx = n + k + 1

    # Add nodes
    for i in range(len(res_graph)):
        G.add_node(i)

    # Add edges based on rGraph adjacency lists
    for i, neighbours in enumerate(res_graph):
        for neighbor in neighbours:
            G.add_edge(i, neighbor)

    # Set position manually for nodes to ensure no overlaps
    pos = {}
    
    # Position nodes with label 'c'
    for idx in range(n):
        pos[idx] = (0.25, idx / (n-1))
    
    # Position nodes with label 'r'
    for idx in range(n, n+k):
        pos[idx] = (0.75, (idx-n) / (k-1))

    # Set position for the Source and Sink
    pos[source_idx] = (0, 0.5)
    pos[sink_idx] = (1, 0.5)

    # Map nodes to labels
    labels = {i: "prov" + str(i - n) if i >= n and i < n+k else "hub" + str(i) for i in range(n + k)}
    labels[source_idx] = 'Source'
    labels[sink_idx] = 'Sink'

    # Draw the graph
    nx.draw(G, pos, labels=labels, with_labels=True, node_color="skyblue", node_size=1000, font_size=10, font_weight='bold', edge_color='gray', width=2.0, alpha=0.6)
    plt.savefig(name + ".png")



def plan_city_a(num_data_hubs, num_service_providers, connections, provider_capacities, preliminary_assignment):
    n = num_data_hubs
    k = num_service_providers
    source, sink = n + k, n + k + 1

    # Initialize residual graph with empty edges. Now n+k+2 to account for the source and sink.
    res_graph = [[] for _ in range(n + k + 2)]

    # For each hub, add a connection from source to the hub.
    for hub in range(n):
        res_graph[source].append(hub)
        res_graph[hub].append(source)

    # Then, for each connection in the "connections", add a connection from hub to provider and from provider to hub.
    for hub, providers in connections.items():
        for provider in providers:
            res_graph[hub].append(provider)
            res_graph[provider].append(hub)

    # Finally, add connections from providers to sink, according to the capacities.
    for provider in range(n, n + k):
        provider_idx = provider
        for _ in range(provider_capacities[provider_idx - n]):
            res_graph[provider_idx].append(sink)
            res_graph[sink].append(provider_idx)
            
    return True