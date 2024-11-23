import heapq

class PuzzleState:
    def __init__(self, board, g, h, parent=None):
        self.board = board
        self.g = g  
        self.h = h  
        self.parent = parent
        self.zero_pos = self.find_zero()  
    
    def find_zero(self):
        for i, val in enumerate(self.board):
            if val == 0:
                return i

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def neighbors(self):
        neighbors = []
        zero_row, zero_col = divmod(self.zero_pos, 3)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        
        for dr, dc in moves:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero_pos = new_row * 3 + new_col
                new_board = self.board[:]
                new_board[self.zero_pos], new_board[new_zero_pos] = new_board[new_zero_pos], new_board[self.zero_pos]
                h_cost = manhattan_distance(new_board)
                neighbors.append(PuzzleState(new_board, self.g + 1, h_cost, self))
                
        return neighbors

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def manhattan_distance(board):
    distance = 0
    for i, val in enumerate(board):
        if val == 0:
            continue
        target_row, target_col = divmod(val - 1, 3)
        current_row, current_col = divmod(i, 3)
        distance += abs(target_row - current_row) + abs(target_col - current_col)
    return distance

def a_star(start_board):
    start_state = PuzzleState(start_board, 0, manhattan_distance(start_board))
    open_list = []
    heapq.heappush(open_list, start_state)
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)
        
        if current_state.is_goal():
            return reconstruct_path(current_state)
        
        closed_set.add(tuple(current_state.board))
        
        for neighbor in current_state.neighbors():
            if tuple(neighbor.board) in closed_set:
                continue
            heapq.heappush(open_list, neighbor)
    
    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

start_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
solution = a_star(start_board)

if solution:
    print("Solution found in {} moves:".format(len(solution) - 1))
    for step in solution:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
else:
    print("No solution found.")
