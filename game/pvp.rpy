label pvp_start: 
    $score = Score() 
    python:
        import threading
        walker = PVPGridWalker()
        
        # Start listening for the other player's moves
        threading.Thread(target=network_listener, args=(walker,), daemon=True).start()
        
        # Set the other player's IP (ask them for it or use a variable)
        opponent_ip = "127.0.0.1" 
    label pvp:
        $ walker = PVPGridWalker()
        call screen pvp_wasd_grid
    label npc_win:
        $ score.add_score("npc")
        "SYSTEM" "Cerberus WIN\n Score: Heracles - [score.score_player] | Cerberus - [score.score_npc]"
        jump pvp_menu
    label player_win:
        $ score.add_score("player")
        "SYSTEM" "Heracles WIN\n Score: Heracles - [score.score_player] | Cerberus - [score.score_npc]"
        jump pvp_menu
    label pvp_menu:
        menu:
            "Играть снова": 
                jump pvp
            "Вернуться в главное меню": 
                return

