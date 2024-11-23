from collections import deque

# Function to check if the state is valid
def is_valid(state):
    # (m, c, b) represents (missionaries, cannibals, boat position)
    left_m, left_c, boat = state
    right_m, right_c = 3 - left_m, 3 - left_c
    
    # Check if missionaries are outnumbered on either side
    if (left_m < left_c and left_m > 0) or (right_m < right_c and right_m > 0):
        return False
    return True

# Function to generate the next possible states
def get_successors(state):
    successors = []
    left_m, left_c, boat = state
    moves = [
        (1, 0),  # One missionary
        (2, 0),  # Two missionaries
        (0, 1),  # One cannibal
        (0, 2),  # Two cannibals
        (1, 1),  # One missionary and one cannibal
    ]
    
    # If the boat is on the left side, try moving people to the right side
    if boat == 1:
        for m, c in moves:
            new_state = (left_m - m, left_c - c, 0)
            if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and is_valid(new_state):
                successors.append(new_state)
    
    # If the boat is on the right side, try moving people to the left side
    else:
        for m, c in moves:
            new_state = (left_m + m, left_c + c, 1)
            if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and is_valid(new_state):
                successors.append(new_state)
    
    return successors

# Function to solve the problem using BFS
def solve():
    # Initial state: (3, 3, 1) -> 3 missionaries, 3 cannibals, boat on the left side
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)  # Goal state: all are on the right side
    
    # Queue for BFS and a set to keep track of visited states
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        
        # If we reach the goal state, return the solution path
        if current_state == goal_state:
            return path + [goal_state]
        
        # Mark the current state as visited
        visited.add(current_state)
        
        # Generate and explore successors
        for successor in get_successors(current_state):
            if successor not in visited:
                queue.append((successor, path + [current_state]))

    return None  # If no solution is found

# Solve the problem and print the solution path
solution = solve()
if solution:
    print("Solution path:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
