label pvp:
    $ walker = PVPGridWalker()
    call screen pvp_wasd_grid
label npc_win:
    "SYSTEM" "Cerberus WIN"
    menu:
        "Играть снова": 
            jump pvp
        "Вернуться в главное меню": 
            return

label player_win:
    "SYSTEM" "Heracles WIN"
    menu:
        "Играть снова": 
            jump pvp
        "Вернуться в главное меню": 
            return
