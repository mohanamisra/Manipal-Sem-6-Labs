import itertools

# FIND NUMERICAL VALUE
def get_value(word, sol):
    val = 0
    fact = 1
    for letter in reversed(word):
        val += fact * sol[letter]
        fact *= 10
    return val

def solve(equation):
    left, right = equation.lower().replace(' ', '').split('=')
    left = left.split('+')

    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(f"REQUIRED MAPPING IS {sol}")


solve('SEND + MORE = MONEY')
