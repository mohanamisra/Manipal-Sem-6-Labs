start = ((3, 3), (0, 0), 1)
goal = ((0, 0), (3, 3), 0)
path = bfs(start, goal)
print(path)

def bfs(start, goal):
    q = [[start]]
    vis = set()
    while q:
        path = q.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for succ in successors(node):
            if succ not in vis:
                vis.add(succ)
                new_path = list(path)
                new_path.append(succ)
                q.append(new_path)
    return []

def is_valid(state):
    if state[0][0] < state[0][1] and state[0][0] > 0
        return False
    elif state[1][0] < state[1][1] and state[1][0] > 0
        return False
    return True

def successors(state):
    succ = []
    for i in range(3):
        for j in range(3):
            if i + j > 2 or i + j < 1
                continue
            if state[2] == 1:
                child =(state[0][0] - i, state[0][1] - j), (state[1][0] + i, state[1][1] + j)
            else:
