




init python:
    class GridWalker:
        def __init__(self):
            # Player Stats
            self.player_idx = 76
            self.hp = 1000
            self.max_hp = 10
            self.closest = [-1]
            # NPC Stats
            self.npc_idx = 4
            self.npc_hp = 10
            self.npc_max_hp = 10
            self.npc_alive = True
            self.byt = [-1]
            self.cols = 9
            self.rows = 9
        def move(self, direction):
            row = self.player_idx // self.rows
            col = self.player_idx % self.cols
            target = self.player_idx

            if direction == "w" and row > 0: target -= self.rows
            elif direction == "s" and row < 8: target += self.rows
            elif direction == "a" and col > 0: target -= 1
            elif direction == "d" and col < 8: target += 1

            


            # Check if moving into the NPC
            if target == self.npc_idx and self.npc_alive:
                #self.attack_npc(10) # Player hits NPC
                self.take_damage(1)  # NPC hits back
                return # Block movement while fighting

            # Move if the tile is empty or NPC is dead
            if target != self.player_idx:
                self.player_idx = target
                renpy.restart_interaction()
            
            
            
        def celltoxycords(self,cell_idx):
            return (cell_idx % self.cols, cell_idx // self.rows)
        def xycordstocell(self,x, y):
            return (y * self.cols + x)

        def attack_npc(self, damage):
            self.npc_hp -= damage
            if self.npc_hp <= 0:
                self.npc_hp = 0
                renpy.jump("smth")
            renpy.restart_interaction()

        def take_damage(self, amount):
            self.hp -= amount
            if self.hp <= 0:
                self.hp=0
                renpy.jump("smth1")
            renpy.restart_interaction()

        def space_attack(self):
            # Вычисляем координаты игрока
            px, py = self.celltoxycords(self.player_idx)
            # Вычисляем координаты NPC
            nx, ny = self.celltoxycords(self.npc_idx)
            
            # Проверяем расстояние: разница по X и Y не должна превышать 1
            # (это затронет 8 клеток вокруг: по горизонтали, вертикали и диагонали)
            if abs(px - nx) <= 1 and abs(py - ny) <= 1:
                self.attack_npc(1)
                
        def dog_attack(self):
            # Вычисляем координаты игрока
            px, py = self.celltoxycords(self.player_idx)
            # Вычисляем координаты NPC
            nx, ny = self.celltoxycords(self.npc_idx)
            self.byt=[self.xycordstocell(nx-1, ny),self.xycordstocell(nx-2, ny),self.xycordstocell(nx+1, ny),self.xycordstocell(nx+2, ny),self.xycordstocell(nx, ny-1),self.xycordstocell(nx, ny-2),self.xycordstocell(nx, ny+1),self.xycordstocell(nx, ny+2),self.xycordstocell(nx-1, ny-1),self.xycordstocell(nx-2, ny-1),self.xycordstocell(nx-1, ny-2),self.xycordstocell(nx-2, ny-2),self.xycordstocell(nx+1, ny-1),self.xycordstocell(nx+2, ny-1),self.xycordstocell(nx+1, ny-2),self.xycordstocell(nx+2, ny-2),self.xycordstocell(nx-1, ny+1),self.xycordstocell(nx-2, ny+1),self.xycordstocell(nx-1, ny+2),self.xycordstocell(nx-2, ny+2),self.xycordstocell(nx+1, ny+1),self.xycordstocell(nx+2, ny+1),self.xycordstocell(nx+1, ny+2),self.xycordstocell(nx+2, ny+2)]
            # Проверяем расстояние: разница по X и Y не должна превышать 1
            
            # (это затронет 8 клеток вокруг: по горизонтали, вертикали и диагонали)
            if abs(px - nx) <= 2 and abs(py - ny) <= 2:
                self.take_damage(3)
                
        def dog_attack1(self):
            px, py = self.celltoxycords(self.player_idx)
            nx, ny = self.celltoxycords(self.npc_idx)
            att1=[self.xycordstocell(nx-1, ny),self.xycordstocell(nx-2, ny),self.xycordstocell(nx-3, ny)]
            att2=[self.xycordstocell(nx-1, ny),self.xycordstocell(nx-2, ny-1),self.xycordstocell(nx-3, ny-2)]
            att3=[self.xycordstocell(nx-1, ny-1),self.xycordstocell(nx-2, ny-2),self.xycordstocell(nx-3, ny-3)]
            att4=[self.xycordstocell(nx-1, ny-1),self.xycordstocell(nx-1, ny-2),self.xycordstocell(nx-1, ny-3)]
            att5=[self.xycordstocell(nx, ny-1),self.xycordstocell(nx, ny-2),self.xycordstocell(nx, ny-3)]
            att6=[self.xycordstocell(nx+1, ny-1),self.xycordstocell(nx+1, ny-2),self.xycordstocell(nx+1, ny-3)]
            att7=[self.xycordstocell(nx+1, ny-1),self.xycordstocell(nx+2, ny-2),self.xycordstocell(nx+3, ny-3)]
            att8=[self.xycordstocell(nx+1, ny),self.xycordstocell(nx+2, ny-1),self.xycordstocell(nx+3, ny-2)]
            att9=[self.xycordstocell(nx+1, ny),self.xycordstocell(nx+2, ny),self.xycordstocell(nx+3, ny)]
            pool=[att1,att2,att3,att4,att5,att6,att7,att8,att9]
            target = self.player_idx
            self.closest = min(pool, key=lambda x: min(abs(i - target) for i in x))
            if target in self.closest:
                self.take_damage(2)