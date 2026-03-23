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






# Игра начинается здесь:

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