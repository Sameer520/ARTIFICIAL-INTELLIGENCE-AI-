import itertools

def calculate_distance(path, distance_matrix):
    total_distance = 0
    num_cities = len(path)
    for i in range(num_cities - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]
    return total_distance

def travelling_salesman(distance_matrix):
    num_cities = len(distance_matrix)
    cities = range(num_cities)
    min_path = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities):
        current_distance = calculate_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm

    return min_path, min_distance

try:
    num_cities = int(input("Enter the number of cities: "))
    if num_cities < 2:
        raise ValueError("Number of cities must be at least 2.")

    distance_matrix = []
    for i in range(num_cities):
        row = list(map(int, input(f"Enter distances for city {i + 1} (space-separated, {num_cities} values): ").split()))
        if len(row) != num_cities:
            raise ValueError(f"Each row must have exactly {num_cities} values.")
        distance_matrix.append(row)

    best_path, best_distance = travelling_salesman(distance_matrix)

    print(f"Optimal Path: {' -> '.join(map(str, best_path))} -> {best_path[0]}")
    print(f"Minimum Distance: {best_distance}")

except ValueError as e:
    print(f"Input Error: {e}")
