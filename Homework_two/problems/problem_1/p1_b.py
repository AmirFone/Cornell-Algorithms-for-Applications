# Problem 1b


def maxsum_tree(vertices, adjacency) -> int:
    n = len(vertices)
    if n == 0:
        return 0

    include = [0 for _ in range(n)]
    exclude = [0 for _ in range(n)]

    def dfs(node, parent = -1):
        # base case
        if not adjacency[node]:
            # Leaf node
            include[node] = vertices[node]
            exclude[node] = 0
            return
        # general case
        include[node] = vertices[node]
        exclude[node] = 0

        for child in adjacency[node]:
            if child == parent:
                continue

            dfs(child, node)

            include[node] += exclude[child]
            exclude[node] += max(include[child], exclude[child])

    dfs(0)
    return max(include[0], exclude[0])