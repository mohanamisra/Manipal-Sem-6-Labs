def dfs(node, graph, visited, dfsOrder):
    dfsOrder.append(node)
    visited[ord(node) - 65] = True

    for child in graph[node]:
        if not visited[ord(child) - 65]:
            dfs(child, graph, visited, dfsOrder)


graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D'],
}

start = 'A'
visited = [False] * len(graph)
dfsOrder = []
dfs(start, graph, visited, dfsOrder)

print(f"Depth First Search Order: {dfsOrder}")
