from collections import defaultdict

def is_bipartite(graph):
    color = defaultdict(int)
    visited_nodes = set()
    nodes = [key for key, value in graph.items()]

    for node, neighbors in graph.items():
        # Assign the first node the color 1.
        if node not in color:
            queue = [node]
            color[node] = 1

            if len(graph[node]) and graph[node][0] in color:
                color[node] = 3 - color[graph[node][0]]

            visited_nodes.add(node)

            while queue:
                current_node = queue.pop(0)
                current_color = color[current_node]

                for neighbor in graph[current_node]:
                    if neighbor not in color:
                        # Toggle the color between 1 and 2.
                        color[neighbor] = 3 - current_color
                        queue.append(neighbor)
                        visited_nodes.add(neighbor)
                    # If the neighbor is already colored and has the same color as the current node, the graph is not bipartite.
                    elif color[neighbor] == current_color:
                        return False

    # Return True if the graph is bipartite.
    return True