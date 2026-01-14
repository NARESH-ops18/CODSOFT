import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human_player = 'O'
        self.ai_player = 'X'

    def print_board(self):
        """Print the current board state"""
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("---------")

    def available_moves(self):
        """Return list of available move positions (0-8)"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position, player):
        """Place player's mark at position if valid"""
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def is_board_full(self):
        """Check if board has no empty spaces"""
        return ' ' not in self.board

    def check_winner(self):
        """Check rows, columns, and diagonals for winner"""
        # Rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return self.board[i]
        # Columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return self.board[i]
        # Diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        return None

    def game_over(self):
        """Game ends if there's a winner or board is full"""
        return self.check_winner() is not None or self.is_board_full()

    def minimax(self, depth, is_maximizing):
        """Core Minimax algorithm - returns best score"""
        winner = self.check_winner()
        
        # Base cases
        if winner == self.ai_player:
            return 1
        if winner == self.human_player:
            return -1
        if self.is_board_full():
            return 0

        # Maximizing player (AI)
        if is_maximizing:
            best_score = float('-inf')
            for move in self.available_moves():
                self.board[move] = self.ai_player
                score = self.minimax(depth + 1, False)
                self.board[move] = ' '
                best_score = max(score, best_score)
            return best_score

        # Minimizing player (human)
        else:
            best_score = float('inf')
            for move in self.available_moves():
                self.board[move] = self.human_player
                score = self.minimax(depth + 1, True)
                self.board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        """Find AI's optimal move using Minimax"""
        best_score = float('-inf')
        best_move = None
        
        for move in self.available_moves():
            self.board[move] = self.ai_player
            score = self.minimax(0, False)
            self.board[move] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move

    def play_game(self):
        """Main game loop"""
        print("Welcome to unbeatable Tic-Tac-Toe!")
        print("You play as 'O', AI plays as 'X'")
        print("Positions: 0|1|2\n         3|4|5\n         6|7|8\n")
        
        # Randomly decide who starts
        current_player = random.choice([self.ai_player, self.human_player])
        
        while not self.game_over():
            self.print_board()
            
            if current_player == self.ai_player:
                print("\nAI is thinking...")
                move = self.get_best_move()
                self.make_move(move, self.ai_player)
                print(f"AI plays at position {move}")
            else:
                while True:
                    try:
                        move = int(input("\nYour move (0-8): "))
                        if 0 <= move <= 8 and self.make_move(move, self.human_player):
                            break
                        print("Invalid move! Try again.")
                    except ValueError:
                        print("Enter a number between 0-8!")
            
            current_player = self.human_player if current_player == self.ai_player else self.ai_player
        
        # Game end
        self.print_board()
        winner = self.check_winner()
        if winner == self.ai_player:
            print("\nAI wins! (Unbeatable!)")
        elif winner == self.human_player:
            print("\nYou win! (Rare against perfect AI)")
        else:
            print("\nIt's a tie!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
