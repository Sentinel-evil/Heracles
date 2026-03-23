




init python:
    class PVPGridWalker:
        def __init__(self):
            # Player Stats
            self.player_idx = 76
            self.hp = 10
            self.max_hp = 10
            
            # NPC Stats
            self.npc_idx = 4
            self.npc_hp = 10
            self.npc_max_hp = 10
            self.npc_alive = True
            
            self.cols = 9
            
        def move(self, direction):
            row = self.player_idx // self.cols
            col = self.player_idx % self.cols
            target = self.player_idx

            if direction == "w" and row > 0: target -= self.cols
            elif direction == "s" and row < 8: target += self.cols
            elif direction == "a" and col > 0: target -= 1
            elif direction == "d" and col < 8: target += 1

            


            # Check if moving into the NPC
            if target == self.npc_idx and self.npc_alive:
                self.attack_npc(1) # Player hits NPC
                #self.take_damage(1)  # NPC hits back
                return # Block movement while fighting

            # Move if the tile is empty or NPC is dead
            if target != self.player_idx:
                self.player_idx = target
                renpy.restart_interaction()
        def move_npc(self, direction):
        

            row = self.npc_idx // self.cols
            col = self.npc_idx % self.cols
            npc_target = self.npc_idx

            if direction == "i" and row > 0: npc_target -= self.cols
            elif direction == "k" and row < 8: npc_target += self.cols
            elif direction == "j" and col > 0: npc_target -= 1
            elif direction == "l" and col < 8: npc_target += 1

            if npc_target == self.player_idx and self.npc_alive:
                #self.attack_npc(1) # Player hits NPC
                self.take_damage(1)  # NPC hits back
                return # Block movement while fighting

            # Prevent NPC from stepping on the Player
            if npc_target != self.player_idx:
                self.npc_idx = npc_target
                renpy.restart_interaction()



        def attack_npc(self, damage):
            self.npc_hp -= damage
            if self.npc_hp <= 0:
                self.npc_hp = 0
                renpy.jump("npc_win")
            renpy.restart_interaction()

        def take_damage(self, amount):
            self.hp -= amount
            if self.hp <= 0:
                self.hp=0
                renpy.jump("player_win")
            renpy.restart_interaction()
#default walker = None