import heapq

class Node:
    def __init__(self, position, g_cost, h_cost, parent=None):
        self.position = position
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def a_star(start, goal, grid):
    open_list = []
    closed_list = set()
    start_node = Node(start, 0, manhattan_distance(start, goal))
    goal_node = Node(goal, 0, 0)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = get_neighbors(current_node.position, grid)
        for neighbor in neighbors:
            if neighbor in closed_list:
                continue
            g_cost = current_node.g_cost + 1
            h_cost = manhattan_distance(neighbor, goal)
            neighbor_node = Node(neighbor, g_cost, h_cost, current_node)

            if not in_open_list(open_list, neighbor_node):
                heapq.heappush(open_list, neighbor_node)

    return None

def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def get_neighbors(position, grid):
    neighbors = []
    x, y = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:
            neighbors.append((new_x, new_y))

    return neighbors

def in_open_list(open_list, node):
    return any(n.position == node.position for n in open_list)

def print_path(path):
    for step in path:
        print(step)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    grid = []
    print("Enter the grid (0 for empty space, 1 for obstacle):")
    for i in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)

    start_x, start_y = map(int, input("Enter the start position (row, col): ").split())
    goal_x, goal_y = map(int, input("Enter the goal position (row, col): ").split())

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    path = a_star(start, goal, grid)

    if path:
        print("Path found:")
        print_path(path)
    else:
        print("No path found.")
