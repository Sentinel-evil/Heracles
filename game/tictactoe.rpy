init python:
    import random

    class TicTacToe:
        def __init__(self):
            self.board = [None] * 9
            self.turn = "X" 
            self.winner = None
            self.message = "Your Turn (X)"

        def player_move(self, index):
           
            if self.board[index] is None and self.winner is None:
                self.board[index] = "X"
                self.check_winner()
                

                if self.winner is None:
                    self.turn = "O"
                    self.message = "Computer Thinking..."
                    renpy.restart_interaction()
                    self.ai_move()

        def ai_move(self):
            empty_slots = [i for i, x in enumerate(self.board) if x is None]
            
            if empty_slots:
                choice = random.choice(empty_slots)
                self.board[choice] = "O"
                self.check_winner()
                
                if self.winner is None:
                    self.turn = "X"
                    self.message = "Your Turn (X)"

        def check_winner(self):
            wins = [
                (0,1,2), (3,4,5), (6,7,8), 
                (0,3,6), (1,4,7), (2,5,8), 
                (0,4,8), (2,4,6)           
            ]
            
            for a, b, c in wins:
                if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                    self.winner = self.board[a]
                    self.message = f"{self.winner} Wins!"
                    return

            if None not in self.board:
                self.winner = "Draw"
                self.message = "It's a Draw!"

default ttt_game = None