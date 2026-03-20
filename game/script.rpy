# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define He = Character('Геракл', color="#c8ffc8")
define Eur = Character('Эврисфей')
define Atl = Character('Атлант')
define Spam = Character('Продовец лучших из лучших телефонов')
define Aid = Character('Аид')
define Cer1 = Character('Первая Голова')
define Cer2 = Character('Вторая Голова')
define Cer3 = Character('Третья Голова')


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
screen tictactoe_game():
    modal True 
    add "#00000080" 
    frame:
        align (0.5, 0.5)
        padding (20, 20)
        vbox:
            spacing 20
            
           
            text "[ttt_game.message]" size 30 xalign 0.5

           
            grid 3 3:
                spacing 10
                for i in range(9):
                    button:
                        xysize (100, 100)
                        background "#444"
                        
                        
                        if ttt_game.board[i] is not None or ttt_game.winner is not None:
                            action NullAction()
                        else:
                            action Function(ttt_game.player_move, i)

                        # Display X, O, or nothing
                        text (ttt_game.board[i] or "") size 50 align (0.5, 0.5) color "#FFF"

            # Close / Reset Buttons
            hbox:
                xalign 0.5
                spacing 20
                
               
                    
                textbutton "Quit":
                    action Return()
# Игра начинается здесь:
screen think():
    text "Ещё Вчера Геракл закончил исполнять свой последний подвиг…":
        align (0.5,0.5)
screen think2():
    text "И вот, отдохнув один день, он вернулся во дворец Эврисфея":
        align (0.5,0.5)


label start:
    scene black
    scene black
    with Dissolve(.5)
    "Голос" "Ещё вчера Геракл закончил исполнять свой последний подвиг…"
    "Голос" "И вот, отдохнув один день, он вернулся во дворец Эврисфея"
    pause .5

    scene трон
    show her_based
    show eur_base
    with Dissolve(.5)

    
    Eur "Ах наконец ты пришел…"
    Eur "Остался один подвиг…"    
    Eur "Тот телефон что ты принёс…"
    Eur "Никуда не годится"
    Eur "Он разряжается всего за два часа…"
    hide eur_base
    show eur_sad
    Eur "Может заставить тебя нести новый?"
    Eur "Хмммм, нет, это слишком скучно…"
    Eur "..."
    Eur "Хмммм"
    Eur "Принеси мне..."
    Eur "..."
    Eur "Того кто меня развлечет..."
    hide eur_sad
    show eur_scream
    Eur "ХОЧУ СОБАЧКУ!1!"
    Eur "Да, неси мне ЦЕРБЕРА, СТРАЖА ПРЕИСПОДНЕЙ"
    pause .5
    scene black
    with Dissolve(.5)
    "Голос" "Выходя из дворца, Геракл решал где же ему искать Цербера…"
    show her_confused 
    He "На той развилке, перед яблоками…"
    He "Был же ещё один путь…"
    He "Кажется он вел к мысу Тенарон…"
    
    scene развилка
    show her_confused
    He "Куда же мне пойти сначала?"
    menu:
        "Налево":
            jump choise1_left
        "Направо":
            jump choise1_right
        "Прямо":
            jump choise1_forward

    label choise1_right:
        He "Возможно Аиду нужно будет подношение…."
        He "Как хорошо что в прошлый раз я нашел короткий путь…"
        scene гора
        show небо:
            ypos -0.7
        show atl_based
        show her_full:
            xpos 0
        Atl "Ааааа, это снова ты… Ты обманул меня в тот раз"
        He "Не волнуйся, в этот раз все будет нормально"
        He "Я снова даю тебе шанс размяться, неси яблоки, я подержу небо"
        Atl "Да, да, я обязательно вернусь с яблоками"
        show her_full:
            linear 1.0 xpos 0.2
        show atl_based:
            linear 0.5 xpos 1.5
        with Dissolve(.5)
        "Голос" "Так он стоял ещё два часа..."
        hide atl_based
        pause .5
        scene black
        with Dissolve(.5)
        return

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
        $ ttt_game = TicTacToe()
        call screen tictactoe_game
        
        
        if ttt_game.winner == "X":
            jump smth
        elif ttt_game.winner == "O":
            "Голос" "Так он проиграл Церберу..."
            "Голос" "И так он лежал ещё два часа..."
            jump smth0
        else:
            He "Ничья?"
            He "переиграем..."
            jump smth0



           
       
        # Ромчик вставь сюда эпичный бит бокс баттл
        #                                            \\\\\\  \\\\   \\  \\
        #                                               \\    \\ \\  \\\\\\
        #                                             \\ \\    \\ \\  \\  \\
        #                                               \\\     \\\\   \\  \\

        # В случае проигрыша пусть геракл упадет и так он лежал ещё два часа и все с начала
        # Падение проговори текстом голоса
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

        label choise3_forward:
            with Dissolve(.5)
            scene трон
            show her_happy
            show cerberus_h
            show eur_sad
            He "Держи свою СОБАЧКУ!1!"
            "Голос" "Однако Цербер выглядел очень..."
            "Голос" "ОЧЕНЬ ГОЛОДНЫМ"
            hide eur_sad
            show eur_scream
            Eur "ААААААААААААААААААААААААААААААА"
            # Тут типо звуки криков вставьте
            with Dissolve(.5)
            scene black
            "Голос" "Так он кричал ещё два часа..."
            return

        label choise3_right:
            with Dissolve(.5)
            scene гора
            show atl_based
            show небо:
                ypos -0.7
            show atl_based
            show her_full:
                xpos 0
            show cerberus_lol
            Atl "Ааааа, это снова ты… Ты обманул меня в тот раз"
            Atl "Ты ещё и с этим чудовищем!?"
            He "Мне нужна твоя помощь, я снова подержу небо, а ты снова принесёшь яблоки"
            He "А пока ты будешь это делать пёс..."
            menu:
                "Будет помогать мне":
                    jump choise4_fail
                "Проконтролирует тебя":
                    jump choise4_look

            label choise4_fail:
                show her_full:
                    linear 1.0 xpos 0.2
                show atl_based:
                    linear 0.5 xpos 1.5
                Atl "Ну раз тебе помогает сам Цербер, то и я помогу"
                with Dissolve(.5)
                scene black
                "Голос" "Атлант так и не вернулся..."
                "Голос" "А Геракл?" 
                "Голос" "Так он стоял ещё 2 часа…" 
                return

            label choise4_look:
                show her_full:
                    linear 1.0 xpos 0.2
                show atl_based:
                    linear 0.5 xpos 1.5
                show cerberus_lol:
                    linear 1.0 xpos 1.5 
                with Dissolve(.5)
                scene black
                "Голос" "Атлант в ужасе от Цербера быстро принес яблоки"
                "Голос" "Сытый от яблок Цербер был уже не так страшен"
                with Dissolve(.5)
                scene трон
                show her_happy
                show cerberus_h
                show eur_base
                He "Держи свою СОБАЧКУ!1!"
                with Dissolve(.5)
                scene good_end
                "Голос" "Цербер и Эврисфей выглядени счастливо"
                "Голос" "Так они играли еще 2 часа…"
                "Голос" "Но это уже совсем другая история..."
                return






    label choise1_left:
        He "Возможно Еврисфею подойдёт просто новый телефон?"
        He "Я не очень то и хочу идти в царство мёртвых..."
        scene аррле
        with Dissolve(.5)
        show timcok_1
        show her_based
        Spam "Здравствуйте!"
        hide timcok_1
        show timcok_2
        Spam "Вижу, вы цените надёжность и узнаваемый стиль. "
        hide timcok_2
        show timcok_3
        Spam "У нас тут есть кое-что столь же неубиваемое, как вы."
        hide timcok_3
        show timcok_4
        Spam "Начнём, может быть, с непромокаемых Apple Watch или ноутбука, которых такой как вы легко унесёт с десяток?"
        hide timcok_4
        show timcok_5
        He "Э-э-э-э"
        show her_confused
        He "Ну-у-у-у"
        hide timcok_5
        show timcok_1
        Spam "Тогда однозначно яблоблоки профессиональный взгляд! всего за 67000 Тенге"
        hide timcok_1
        show timcok_2
        Spam "Для бога — копейки! Чтобы смотреть прямую трансляцию с Олимпа в дополненной реальности. И биометрия по радужке — верификация на уровне божественности."
        He "Это не для меня..."
        hide timcok_2
        show timcok_3
        Spam "Ооо, дружище, это не имеет значения, заряда хватит на целый день, я уверен - ты не пожалеешь"
        "Голос" "Геракл был весьма смущен, однако понёс яблоблоки профессиональный взгляд Эврисфею"
        scene развилка
        show her_confused
        He "Куда же отправится теперь?" 
        with Dissolve(.5)
        menu:
            "Налево":
                jump choise2_left
            "Направо":
                jump choise1_right
            "Прямо":
                jump choise1_forward
            "Попятится в тронный зал":
                jump choise2_fail

    label choise2_left:
        scene аррле
        with Dissolve(.5)
        show timcok_1
        show her_confused
        Spam "ЧТО? Вам нужно что-то еще?"
        hide timcok_1
        show timcok_2
        Spam 'Быть может вы боитесь, что наш "Взгляд" устареет пока вы его несете?'
        hide timcok_2
        show timcok_3
        Spam "Возможно вы хотите AMAZING NEW DESIGN?"
        hide timcok_3
        show timcok_4
        Spam "Возмьмите новыый ЯТелефон 2077 про ультра новейший процессор камеры не сравнятся с прошлогодней моделью и всякими дройдами всеволишь за всю вашу зарплату?"
        hide timcok_4
        show timcok_5
        Spam "Берите это все в 1 корпусе! Несите его быстрее!!! у вас есть 3 часа пока мы не выпустим новый"
        hide timcok_5
        show timcok_1
        scene трон
        show her_happy
        show eur_base
        He "Вот тебе телефон!"
        hide eur_base
        show eur_sad
        Eur "УУУ, я же просил СОБАЧКУ!1!"
        show timcok_1
        hide eur_sad
        show eur_scream
        Spam "НО ЭТО ЖЕ новыый ЯТелефон 2077 про ультра новейший процессор камеры не сравнятся с прошлогодней моделью и всякими дройдами!!!"
        show eur_sad
        hide eur_scream
        hide timcok_1
        Eur "Ммм..."
        Eur "Гмм..."
        Eur "Хмм..."
        hide eur_sad
        show eur_base
        Eur "Нууу, раз он новый ЯТелефон 2077 про ультра, то так уж и быть"
        Eur "Я поиграю в Адские нырялы 3"
        "Голос" "И так он еще 3 часа пытался найти вечеринку"
        show black
        with Dissolve(.8)
        "Голос" "И так он играл еще 2 часа..."
        return

    label choise2_fail:
        scene трон
        with Dissolve(.5)
        show her_based
        show eur_base
        He "Вот тебе телефон!"
        hide eur_base
        show eur_scream
        Eur "УУУ, я же просил СОБАЧКУ!1!"
        Eur "Снова ты приносишь мне не то что требовалось"
        Eur "ДА КАК ТЕБЕ ВООБЩЕ ХВАТИЛО НАГЛОСТИ НА ТАКОЙ ПОСТУПОК!?"
        show black
        with Dissolve(.8)
        "Голос" "Так он ругался ещё 2 часа…"
        return

    label choise3_left:
        He "Нет. Туда не пустят с животными"
        jump choise0
    return