# CHECK FOR VALIDITIY OF A STATE
def valid(state):
    if state[0][0] < state[0][1] and state[0][0] > 0:
        return False
    elif state[1][0] < state[1][1] and state[1][0] > 0:
        return False
    return True

# GENERATE SUCCESSOR NODES
def successor(state):
    children = []

    for i in range(3):
        for j in range(3):
            if i + j < 1 or i + j > 2:
                continue
            if state[2] == 1:
                child = ((state[0][0] - i, state[0][1] - j), (state[1][0] + i, state[1][1] + j), 0)
            else:
                child = ((state[0][0] + i, state[0][1] + j), (state[1][0] - i, state[1][1] - j), 1)
            if valid(child):
                children.append(child)
    return children

# SEARCH THE STATE SPACE
def bfs(start, goal):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        for child in successor(node):
            if child not in visited:
                visited.add(child)
                new_path = list(path)
                new_path.append(child)
                queue.append(new_path)
    return []

initial = ((3, 3), (0, 0), 1)
goal = ((0, 0), (3, 3), 0)
paths = bfs(initial, goal)

if paths:
    for state in paths:
        print(state)
else:
    print('No path found')
