import random

x_range = [x for x in range(10)]

def hill_climb_search(f, neighbour_f, max_iter = 1000):
    curr = random.choice(list(x_range))
    for i in range(max_iter):
        neighbours = neighbour_f(curr)
        next_neighbour = max(neighbours, key = lambda x: f(x))
        if f(next_neighbour) <= f(curr):
            break
        curr = next_neighbour
    return curr, f(curr)


def f(x):
    return -x**2


def neighbour_f(x):
    return [x + dx for dx in [-0.1, 0, 0.1]]


best_sol, best_val = hill_climb_search(f, neighbour_f)
print(f"Best solution x = {best_sol} and best value f(x) = {best_val}")