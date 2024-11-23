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

    def check_win(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def check_draw(self):
        return ' ' not in self.board

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

def play_game():
    game = TicTacToe()
    game.print_board()

    while True:
        try:
            position = int(input(f"Player {game.current_player}, enter a position (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if game.make_move(position):
            game.print_board()
            if game.check_win():
                print(f"Player {game.current_player} wins!")
                break
            if game.check_draw():
                print("It's a draw!")
                break
            game.switch_player()
        else:
            print("This position is already taken. Try again.")

if __name__ == "__main__":
    play_game()
