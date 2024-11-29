from queue import PriorityQueue

def uniform_cost_search(start, goal, graph):
    frontier = PriorityQueue()
    explored = set()
    frontier.put((start, 0))

    while not frontier.empty():
        curr_node, curr_cost = frontier.get()
        if curr_node == goal:
            return curr_cost
        explored.add(curr_node)
        for neighbour, cost in graph[curr_node].items():
            new_cost = curr_cost + cost
            frontier.put((neighbour, new_cost))
    return -1

graph = {
'A': {'B': 2, 'C': 1},
'B': {'D': 2},
'C': {'D': 3, 'E': 4},
'D': {'F': 1},
'E': {'F': 5},
'F': {}
}

start = 'A'
goal = 'F'

print(uniform_cost_search(start, goal, graph))