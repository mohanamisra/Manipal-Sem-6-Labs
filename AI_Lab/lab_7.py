# THE DFS USER FUNCTION
def solve(sizes, start, target):
    explored = set()
    start_state = (start)
    path = dfs(start_state, target, sizes, explored)
    return path

# THE DFS FUNCTION
def dfs(curr_state, target, sizes, explored):
    j1, j2 = curr_state

    if j1 == target or j2 == target:
        return [curr_state]
    explored.add(curr_state)
    for child in successors(curr_state, sizes):
        if child not in explored:
            path = dfs(child, target, sizes, explored)
            if path is not None:
                return [curr_state] + path
    return None


# VALIDITY CHECKER
def is_valid(sizes, state):
    j1_max, j2_max = sizes
    j1, j2 = state
    return 0 <= j1 <= j1_max and 0 <= j2 <= j2_max


# SUCCESSOR GENERATOR
def successors(state, sizes):
    j1, j2 = state
    j1_max, j2_max = sizes

    succ = []
    succ.append((j1, j2_max))
    succ.append((j1_max, j2))
    succ.append((0, j2))
    succ.append((j1, 0))

    pour = min(j1, j2_max - j2)
    succ.append((j1 - pour, j2 + pour))
    pour = min(j2, j1_max - j1)
    succ.append((j1 + pour, j2 - pour))

    return [s for s in succ if is_valid(sizes, s)]


jugs = (4, 3)
target = 2
start = (0, 0)
path = solve(jugs, start, target)
print(path)
