import heapq

def a_star(start, goal, graph, heuristic):
    frontier = [(heuristic[start], start)]
    explored = set()
    cost = {start: 0}
    path = {start: None}

    while frontier:
        _, curr = heapq.heappop(frontier)
        if curr == goal:
            path_list = [curr]
            while path[curr] != None:
                path_list.append(path[curr])
                curr = path[curr]
            path_list.reverse()
            return path_list
        explored.add(curr)
        for neighbour in graph[curr]:
            new_cost = cost[curr] + graph[curr][neighbour]
            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                priority = new_cost + heuristic[neighbour]
                heapq.heappush(frontier, (priority, neighbour))
                path[neighbour] = curr
    return None

graph = {
'A' : {'B':5, 'C':10},
'B' : {'D':15},
'C' : {'D':20},'D':{}
}

heuristic = {
'A':15,
'B':10,
'C':5,
'D':0
}

start = 'A'
goal = 'D'

path = a_star(start, goal, graph, heuristic)
print(path)
