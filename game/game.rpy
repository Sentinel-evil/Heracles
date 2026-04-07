




init python:
    import math
    import time
    import threading
    import random
    class GridWalker:
        def __init__(self):
            self.player_idx = 76
            self.hp = 10
            self.max_hp = 10
            self.closest = [-1]
            self.npc_idx = 4
            self.npc_hp = 10
            self.npc_max_hp = 10
            self.npc_alive = True
            self.byt = [-1]
            self.cols = 9
            self.rows = 9
            self.time_attack = 1
            self.time_dog_attack = 2
            self.time_dog_attack1 = 1.5
            self.sharpness = 3
            self.sharpness1 = 2
            self.rand_range_for_dog_attack1 = [1, 2, 3,4]
            self.rand_max=5
            self.bump_damage = 1
            self.keep_attacking = True
        def thr_move(self, direction):
            def move(direction):
                row = self.player_idx // self.rows
                col = self.player_idx % self.cols
                target = self.player_idx

                if direction == "w" and row > 0: target -= self.rows
                elif direction == "s" and row < 8: target += self.rows
                elif direction == "a" and col > 0: target -= 1
                elif direction == "d" and col < 8: target += 1
                if target == self.npc_idx and self.npc_alive:
                    self.take_damage(self.bump_damage)
                    return
                if target != self.player_idx:
                    self.player_idx = target
                    renpy.restart_interaction()
            threading.Thread(target=move, args=(direction,)).start()
            
            
        def take_cords(self):
            # Вычисляем координаты игрока
            px, py = self.celltoxycords(self.player_idx)
            nx, ny = self.celltoxycords(self.npc_idx)
            return px, py, nx, ny
        def celltoxycords(self,cell_idx):
            return (cell_idx % self.cols, cell_idx // self.rows)
        def xycordstocell(self,x, y):
            return (y * self.cols + x)

        def attack_npc(self, damage):
            self.npc_hp -= damage
            if self.npc_hp <= 0:
                self.npc_hp = 0
                self.hp = 1000
                self.keep_attacking = False
                renpy.invoke_in_main_thread(renpy.jump, "smth")
            #else:
                #renpy.invoke_in_main_thread(renpy.restart_interaction)

        def take_damage(self, amount):
            self.hp -= amount
            if self.hp <= 0:
                self.hp=1000
                self.npc_hp = 1000
                self.keep_attacking = False
                renpy.invoke_in_main_thread(renpy.jump, "smth1")
            #else:
                #renpy.invoke_in_main_thread(renpy.restart_interaction)

        def space_attack(self):
            px, py = self.celltoxycords(self.player_idx)
            nx, ny = self.celltoxycords(self.npc_idx)
            if abs(px - nx) <= 1 and abs(py - ny) <= 1:
                self.attack_npc(1)
        def thr_space_attack(self):
            threading.Thread(target=self.space_attack).start()
        def byt_count(self):
            px, py, nx, ny = self.take_cords()
            byyt = [
                self.xycordstocell(nx + dx, ny + dy)
                for dx in range(-2, 3)
                for dy in range(-2, 3)
                if not (dx == 0 and dy == 0)
                ]
            return byyt
        def dog_attack(self):
            px, py, nx, ny = self.take_cords()
            self.byt = self.byt_count()
            time.sleep(self.time_dog_attack)
            px, py, nx, ny =self.take_cords()
            if abs(px - nx) <= 2 and abs(py - ny) <= 2:
                self.take_damage(self.sharpness)
            self.byt = []
        def thr_dog_attack(self):
            threading.Thread(target=self.dog_attack).start()
        def dog_attack1(self):
            px, py, nx, ny = self.take_cords()
            target = self.target()
            closestpoint = self.closestpoint()
            self.closest = [int((y * self.rows) + x) for x, y in closestpoint]
            time.sleep(self.time_dog_attack1)
            px, py, nx, ny =self.take_cords()
            target = (px,py)
            if target in closestpoint:
                self.take_damage(self.sharpness1)
            self.closest = []
        def thr_dog_attack1(self):
            threading.Thread(target=self.dog_attack1).start()
        def dist(self, p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        def pool_var(self):
                px, py, nx, ny = self.take_cords()
                att1=[(nx-1, ny),(nx-2, ny),(nx-3, ny)]
                att2=[(nx-1, ny),(nx-2, ny+1),(nx-3, ny+2)]
                att3=[(nx-1, ny+1),(nx-2, ny+2),(nx-3, ny+3)]
                att4=[(nx-1, ny+1),(nx-1, ny+2),(nx-1, ny+3)]
                att5=[(nx, ny+1),(nx, ny+2),(nx, ny+3)]
                att6=[(nx+1, ny+1),(nx+1, ny+2),(nx+1, ny+3)]
                att7=[(nx+1, ny+1),(nx+2, ny+2),(nx+3, ny+3)]
                att8=[(nx+1, ny),(nx+2, ny+1),(nx+3, ny+2)]
                att9=[(nx+1, ny),(nx+2, ny),(nx+3, ny)]
                att10=[(nx-1, ny+1),(nx-2, ny+2),(nx-2, ny+3)]
                att11=[(nx+1, ny+1),(nx+2, ny+2),(nx+2, ny+3)]
                att12=[(nx-1, ny),(nx-2, ny),(nx-3, ny+1)]
                att13=[(nx+1, ny),(nx+2, ny),(nx+3, ny+1)]
                att14=[(nx-1, ny),(nx-2, ny-1),(nx-3, ny-2)]
                att15=[(nx-1, ny-1),(nx-2, ny-2),(nx-3, ny-3)]
                att16=[(nx-1, ny-1),(nx-1, ny-2),(nx-1, ny-3)]
                att17=[(nx, ny-1),(nx, ny-2),(nx, ny-3)]
                att18=[(nx+1, ny-1),(nx+1, ny-2),(nx+1, ny-3)]
                att19=[(nx+1, ny-1),(nx+2, ny-2),(nx+3, ny-3)]
                att20=[(nx+1, ny),(nx+2, ny-1),(nx+3, ny-2)]
                att21=[(nx-1, ny-1),(nx-2, ny-2),(nx-2, ny-3)]
                att22=[(nx+1, ny-1),(nx+2, ny-2),(nx+2, ny-3)]
                att23=[(nx-1, ny),(nx-2, ny),(nx-3, ny-1)]
                att24=[(nx+1, ny),(nx+2, ny),(nx+3, ny-1)]
                pool=[att1,att2,att3,att4,att5,att6,att7,att8,att9,att10,att11,att12,att13,att14,att15,att16,att17,att18,att19,att20,att21,att22,att23,att24]
                return pool
        def closestpoint(self):
            pool = self.pool_var()
            target = self.target()
            closestpoint = min(pool, key=lambda path: min(self.dist(point, target) for point in path))
            return closestpoint
        def target(self):
            px, py, nx, ny = self.take_cords()
            target = (px,py)
            return target
        def choice(self):
            px, py, nx, ny = self.take_cords()
            target = (px,py)
            closestpoint = self.closestpoint()
            byt = self.byt_count()
            if target in closestpoint:
                threading.Thread(target=self.dog_attack1).start()
            if self.xycordstocell(px,py) in byt:
                rand_num = random.randint(1, self.rand_max)
                if rand_num in self.rand_range_for_dog_attack1:
                    threading.Thread(target=self.dog_attack1).start()
                else:
                    threading.Thread(target=self.dog_attack).start()
        def constant_attack(self):
            def attack():
                while self.keep_attacking:
                    time.sleep(self.time_attack)
                    self.choice()
            threading.Thread(target=attack).start()