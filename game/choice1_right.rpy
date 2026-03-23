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