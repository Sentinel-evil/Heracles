




init python:
    import socket
    import json
    import threading
    import time
    class PVPGridWalker:
        def __init__(self):
            # Player Stats
            self.player_idx = 76
            self.hp = 10
            self.max_hp = 10
            self.closest = [-1]
            self.byt = [-1]
            self.npc_idx = 4
            self.npc_hp = 10
            self.npc_max_hp = 10
            self.rows = 9
            self.cols = 9

        def get_state(self):
            state = {
                "player_idx": self.player_idx,
                "hp": self.hp,
                "npc_idx": self.npc_idx,
                "npc_hp": self.npc_hp,
            }
            return json.dumps(state)

        def apply_state(self, json_data):
            data = json.loads(json_data)
            self.player_idx = data["player_idx"]
            self.hp = data["hp"]
            self.npc_idx = data["npc_idx"]
            self.npc_hp = data["npc_hp"]
            self.npc_alive = data["npc_alive"]
            renpy.restart_interaction() # Refreshes the Ren'Py screen

        
        def thr_move(self, direction):    
            def move(direction):
                row = self.player_idx // self.rows
                col = self.player_idx % self.cols
                target = self.player_idx

                if direction == "w" and row > 0: target -= self.rows
                elif direction == "s" and row < 8: target += self.rows
                elif direction == "a" and col > 0: target -= 1
                elif direction == "d" and col < 8: target += 1

                


                # Check if moving into the NPC
                if target == self.npc_idx:
                    self.attack_npc(1)
                    return 
                if target != self.player_idx:
                    self.player_idx = target
                    send_update(self.get_state(), opponent_ip)
                    renpy.restart_interaction()
                send_update(self.get_state(), opponent_ip)
            threading.Thread(target=move, args=(direction,)).start()
        def thr_move_npc(self, direction):
            def move(direction):
                row = self.npc_idx // self.rows
                col = self.npc_idx % self.cols
                npc_target = self.npc_idx

                if direction == "i" and row > 0: npc_target -= self.rows
                elif direction == "k" and row < 8: npc_target += self.rows
                elif direction == "j" and col > 0: npc_target -= 1
                elif direction == "l" and col < 8: npc_target += 1

                if npc_target == self.player_idx:
                    self.take_damage(1)
                    
                    return 
                if npc_target != self.player_idx:
                    self.npc_idx = npc_target
                    send_update(self.get_state(), opponent_ip)
                    renpy.restart_interaction()
                send_update(self.get_state(), opponent_ip)
            threading.Thread(target=move, args=(direction,)).start()
        
        def take_cords(self):
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
                renpy.jump("player_win")
            send_update(self.get_state(), opponent_ip)
            renpy.restart_interaction()

        def take_damage(self, amount):
            self.hp -= amount
            if self.hp <= 0:
                self.hp=0
                renpy.jump("npc_win")
            send_update(self.get_state(), opponent_ip)
            renpy.restart_interaction()
        def thr_space_attack(self):
            def space_attack():
                px, py = self.celltoxycords(self.player_idx)
                nx, ny = self.celltoxycords(self.npc_idx)
                if abs(px - nx) <= 1 and abs(py - ny) <= 1:
                    self.attack_npc(1)
            threading.Thread(target=space_attack).start()
        def thr_dog_attack(self):
            def dog_attack():
                px, py, nx, ny = self.take_cords()
                self.byt = [
                    self.xycordstocell(nx + dx, ny + dy)
                    for dx in range(-2, 3)
                    for dy in range(-2, 3)
                    if not (dx == 0 and dy == 0)
                    ]
                time.sleep(0.5)
                px, py, nx, ny =self.take_cords()
                if abs(px - nx) <= 2 and abs(py - ny) <= 2:
                    self.take_damage(1)
                self.byt = []
            threading.Thread(target=dog_attack).start()
        def thr_dog_attack1(self):   
            def dog_attack1():
                px, py, nx, ny = self.take_cords()
                target = (px,py)
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
                def dist(p1, p2):
                    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
                closestpoint = min(pool, key=lambda path: min(dist(point, target) for point in path))
                self.closest = [int((y * self.rows) + x) for x, y in closestpoint]
                time.sleep(5)
                px, py, nx, ny =self.take_cords()
                target = (px,py)
                if target in closestpoint:
                    self.take_damage(1)
                self.closest = []
            threading.Thread(target=dog_attack1).start()