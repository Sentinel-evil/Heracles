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