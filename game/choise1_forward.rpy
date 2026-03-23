label choise1_forward:
        He "Возможно не стоит отвелекаться на всякую чепуху"
        He "В прошлый раз я уже потерял кучу времени перепутав стороны указателя"
        scene мыс тенарон
        with Dissolve(.5)
        "Голос" "Приближаясь к мысу, Геракл чувствовал нарастающий холод.."
        He "Нужно только зажмуриться" 
        show her_blind 
        "Голос" "Вода отдавала зеленым оттенком и от неё исходило зловещее свечение"
        He "Разбежаться..." 
        "Голос" "И все же Гераклу казалось что он выбрал верный путь…" 
        He "И ПРЫГПУТЬ ВНИЗ" 
        scene подземка
        show her_based
        He "Ну... вроде я на месте" 
        hide her_blind
        show her_based
        He "АИИИИИД" 
        He "АИИИИИИИИИИД ТЫ ТУТ ????" 
        show hades 
        Aid "Если ты ещё не забыл, мне запрещено покидать это место." 
        Aid "Что же заставило тебя отвлечь меня от такого увлекательного занятия, как выгуливание собаки?" 
        He "Мне нужен твой пёс"
        He "Эврисфей попросил принести его"
        hide hades
        show hades_angry
        Aid "ТАК ТЕБЕ НУЖЕН МОЙ ЦЕРБЕР!?!" 
        hide hades_angry
        show hades
        Aid "Впрочем ладно, я и так не успеваю за ним следить, он хочет есть в три раза сильнее других собак" 
        hide hades 
        show hades_visionary
        Aid "Да и гулять я с ним не успеваю, ходят тут всякие." 
        hide hades_visionary
        show hades
        Aid "Но будет одно условие, пёс он буйный, однако верный" 
        Aid "Если сможешь победить его без оружия, он сам за тобой последует и будет выполнять указания" 
        He "Ты думаешь у меня получится?" 
        Aid "Мне будет смешно на это смотреть, впрочем, после боя я тебя не навещу, у меня много работы." 
        hide hades
        "Голос" "Аид скрылся, позвав Цербера" 
        with Dissolve(.5)
        show cerberus
        Cer1 "Гав, РРРРРР"
        Cer2 "РРРРР, Гав" 
        Cer3 "Делу время...."
        label smth0:
        $ walker = GridWalker()
        call screen wasd_grid
        jump smth
        #$ ttt_game = TicTacToe()
        #call screen tictactoe_game
        
        
        #if ttt_game.winner == "X":
        #        jump smth
        #elif ttt_game.winner == "O":
                
        #        jump smth1
        #else:
        #        He "Ничья?"
        #        He "переиграем..."
        
        #        jump smth1
        label smth1:
                "Голос" "Так он проиграл Церберу..."
                "Голос" "И так он лежал ещё два часа..."
                jump smth0
        label smth:
            
        "Голос" "Так Геракл победил Цербера и отправился дальше"
        with Dissolve(.5)
        scene развилка
        show her_confused
        show cerberus_h
        He "Аид говорил что-то про то что Цербер голоден..."
        label choise0:
                menu:
                        "Налево":
                                jump choise3_left
                        "Направо":
                                jump choise3_right
                        "Попятится в тронный зал":
                                jump choise3_forward
