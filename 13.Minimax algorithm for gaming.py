import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def print_board(self):
        print("\n")
        for i in range(3):
            print(f" {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ")
            if i < 2:
                print("---+---+---")
        print("\n")
    
    def is_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def make_move(self, position, player):
        self.board[position] = player

    def undo_move(self, position):
        self.board[position] = ' '

    def minimax(self, depth, is_maximizing_player):
        if self.is_winner('X'):
            return 1
        elif self.is_winner('O'):
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing_player:
            best = -math.inf
            for move in self.available_moves():
                self.make_move(move, 'X')
                best = max(best, self.minimax(depth + 1, False))
                self.undo_move(move)
            return best
        else:
            best = math.inf
            for move in self.available_moves():
                self.make_move(move, 'O')
                best = min(best, self.minimax(depth + 1, True))
                self.undo_move(move)
            return best

    def best_move(self):
        best_val = -math.inf
        move = -1
        for i in self.available_moves():
            self.make_move(i, 'X')
            move_val = self.minimax(0, False)
            self.undo_move(i)
            if move_val > best_val:
                best_val = move_val
                move = i
        return move

def play_game():
    game = TicTacToe()
    game.print_board()

    while True:
        if game.current_player == 'X':
            move = game.best_move()
            print(f"Player X (AI) chooses position {move + 1}")
            game.make_move(move, 'X')
        else:
            move = int(input(f"Player O, enter a position (1-9): ")) - 1
            if game.board[move] != ' ':
                print("Invalid move! Try again.")
                continue
            game.make_move(move, 'O')

        game.print_board()

        if game.is_winner('X'):
            print("Player X (AI) wins!")
            break
        elif game.is_winner('O'):
            print("Player O wins!")
            break
        elif game.is_draw():
            print("It's a draw!")
            break

        game.current_player = 'O' if game.current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
