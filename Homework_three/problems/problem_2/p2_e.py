def plan_city_e(num_data_hubs, num_service_providers, connections, provider_capacities, preliminaryAssignment):
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

    # Try to assign each data hub to a service provider via DFS
    assignment = [-1] * n
    def dfs(u, visited):
        print(f'Visiting node {u}')  # Debug print
        visited[u] = True
        if u == sink:  # if reached sink, return True indicating a path exists
            return True
        for v in res_graph[u]:
            if not visited[v] and dfs(v, visited):
                if u < n:
                    assignment[u] = v
                    res_graph[u].remove(v)
                    provider_capacities[v] -= 1
                    print(f'Assigning node {v} to {u}')  # Debug print
                    if provider_capacities[v] > 0:
                        res_graph[v].append(sink)
                return True
        return False 

    for hub in range(n):
        visited = [False] * (n + k + 2)
        if not dfs(hub, visited):
            print(f'Node {hub} is not connected\n')  # Debug print
            for provider in range(n, n + k):
                visited[provider] = False
            if not dfs(source, visited):
                print("Not all Data Hubs connected to a Service Provider")
                return [0] * num_data_hubs + [int(provider_capacities[i] <= 0) for i in range(n, n + k)]
   
    print(f'All nodes are connected\n')  # Debug print
    return assignment