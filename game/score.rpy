init python:
    class Score:
        def __init__(self):
            self.score_npc = 0
            self.score_player = 0
        def add_score(self,player):
            if player == "npc":
                self.score_npc += 1
            elif player == "player":
                self.score_player += 1