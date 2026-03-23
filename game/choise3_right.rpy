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
