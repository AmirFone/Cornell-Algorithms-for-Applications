def plan_city_d(num_data_hubs, num_service_providers, connections, provider_capacities, preliminaryAssignment):
    n = num_data_hubs
    k = num_service_providers
    source, sink = n + k, n + k + 1  

    # Create residual graph
    res_graph = [[] for _ in range(n + k + 2)]
    for hub in range(n):
        res_graph[source].append(hub)
        for provider in connections[hub]:
            res_graph[hub].append(provider)
    for i, capacity in enumerate(provider_capacities[n:], start=n):
        if capacity > 0:
            res_graph[i].append(sink) 

    # Apply preliminary assignment
    for hub, provider in preliminaryAssignment.items():
        if provider in res_graph[hub]:
            res_graph[hub].remove(provider)
            provider_capacities[provider] -= 1
  
    # Check connectivity of every data hub via DFS
    def dfs(u, visited):
        # print(f'Visiting node {u}')  # Debug print
        visited[u] = True
        if u == sink:  # if reached sink, return True indicating a path exists
            return True
        for v in res_graph[u]:
            if not visited[v] and dfs(v, visited):
                return True
        return False 

    for hub in range(n):
        visited = [False] * (n + k + 2)
        if not dfs(hub, visited):
            # print(f'Node {hub} is not connected\n')  # Debug print
            return False

    # print(f'All nodes are connected\n')  # Debug print
    return True
