class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  
        self.current_player = 'X'

    def print_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def is_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)               
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def play(self):
        while True:
            self.print_board()
            try:
                move = int(input(f"Player {self.current_player}, enter a position (1-9): ")) - 1
                if self.board[move] != ' ':
                    print("Position already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            self.board[move] = self.current_player
            if self.is_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break

            
            self.current_player = 'O' if self.current_player == 'X' else 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
