from collections import deque

def is_solvable(m, n, d):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return d <= max(m, n) and d % gcd(m, n) == 0

def bfs(m, n, d):
    queue = deque()
    queue.append((0, 0))
    visited = set()
    visited.add((0, 0))
    parent = {}
    parent[(0, 0)] = None

    while queue:
        (a, b) = queue.popleft()

        if a == d or b == d:
            return reconstruct_path((a, b), parent)

        next_states = [
            (m, b),
            (a, n),
            (0, b),
            (a, 0),
            (min(a + b, m), b - (min(a + b, m) - a)),
            (a - (min(a + b, n) - b), min(a + b, n))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parent[state] = (a, b)

    return None

def reconstruct_path(state, parent):
    path = []
    while state:
        path.append(state)
        state = parent[state]
    return path[::-1]

def solve_water_jug(m, n, d):
    if not is_solvable(m, n, d):
        return "No solution is possible."
    solution = bfs(m, n, d)
    if solution:
        return f"Solution found in {len(solution) - 1} steps:\n" + "\n".join(f"Jug 1: {a}L, Jug 2: {b}L" for a, b in solution)
    else:
        return "No solution found."

if __name__ == "__main__":
    m = 4
    n = 3
    d = 2
    print(solve_water_jug(m, n, d))
