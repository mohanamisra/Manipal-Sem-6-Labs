graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': [],
}

visited = [False] * len(graph)
q = []
bfsOrder = []
start = 'A'

q.append(start)
visited[ord(start) - 65] = True

while len(q) > 0:
    node = q.pop(0)
    bfsOrder.append(node)

    for child in graph[node]:
        if visited[ord(child) - 65] is False:
            visited[ord(child) - 65] = True
            q.append(child)

print(f"Breadth First Search Order: {bfsOrder}")