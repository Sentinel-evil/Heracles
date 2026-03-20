init python:
    class GridWalker:
        def __init__(self):
            self.player_idx = 76
            self.cols = 9
            self.rows = 9

        def move(self, direction):
            
            col = self.player_idx % self.cols
            row = self.player_idx // self.cols
            
            target = self.player_idx

            if direction == "w" and row > 0:
                target -= self.cols
            elif direction == "s" and row < 8: 
                target += self.cols
            elif direction == "a" and col > 0:
                target -= 1
            elif direction == "d" and col <8:
                target += 1
            
           
            if target != self.player_idx:
                self.player_idx = target
                renpy.restart_interaction()


default walker = None

