import heapq

heuristic = {
    'A': 5,
    'B': 4,
    'C': 30,
    'D': 2,
    'E': 0,
}

graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': [('E', 7)],
    'E': []
}

def best_first_search(heuristic, graph, start, goal):
    # INITIALISATION
    open_list = [(heuristic[start], start, [start])]
    visited = set()

    # MAIN LOOP
    while open_list:
        _, curr_node, curr_path = heapq.heappop(open_list)
        if curr_node == goal:
            return curr_path
        visited.add(curr_node)

        # EXPAND SUCCESSORS
        for neighbour, cost in graph.get(curr_node, []):
            if neighbour not in visited:
                heapq.heappush(open_list, (heuristic[neighbour], neighbour, curr_path + [neighbour]))

    return None

start = 'A'
goal = 'E'
print(best_first_search(heuristic, graph, start, goal))
