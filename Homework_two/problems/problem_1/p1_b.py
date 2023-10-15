# Problem 1b


def maxsum_tree(vertices, adjacency) -> int:
    def dfs(node, parent):
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
            if child != parent:
                dfs(child, node)
                include[node] += exclude[child]
                exclude[node] += max(include[child], exclude[child])

    n = len(vertices)
    if n == 0:
        return 0

    include = [0] * n
    exclude = [0] * n
    # Starting the dynamic programming from the root node and no parent
    dfs(0, -1)

    # The solution is the maximum at the root node
    return max(include[0], exclude[0])