import datetime
import random


def hello():
    now = datetime.datetime.now()
    helloList = [
        'Здравствуй, любимая',
        'Приветик.',
        'Привет, зайка моя.',
        'Салам алейкум, писюлька',
        'Привет, писька',
        'Хелооу, моя маленькая.',
        'Здравствуй, свет моего мира',
        'Приффки',
        'Здравствуй, золотая моя',
        'Привет, мой ангел',
        'Приветсвую, принцесса моя',
    ]
    helloMorningList = [
        'Доброе утро, любимая',
        'Доброе утро.',
        'Доброе утро, зайка моя.',
        'Салам алейкум, писюлька. Доброе утро!',
        'Доброе утро, писька!',
        'Доброе утро, моя маленькая!',
        'Свет моего мира, доброе утро!',
        'Приффки',
        'Доброе утро, золотая моя',
        'Доброе утро, мой ангел',
        'Доброе утро, принцесса моя',
    ]
    helloEveningList = [
        'Добрый вечер, любимая',
        'Добрый вечер, луна моя',
        'Добрый вечер, зайка моя.',
        'Салам алейкум, писюлька. Добрый вечер!',
        'Добрый вечер, писька!',
        'Добрый вечер, моя маленькая!',
        'Свет моего мира, Добрый вечер!',
        'Приффки',
        'Добрый вечер, золотая моя',
        'Добрый вечер, мой ангел',
        'Добрый вечер, принцесса моя',
    ]
    helloNightList = [
        'Доброй ночи, любимая',
        'Доброй ночи, луна моя',
        'Доброй ночи, зайка моя.',
        'Салам алейкум, писюлька. Добрый вечер!',
        'Доброй ночи, писька!',
        'Доброй ночи, моя маленькая!',
        'Свет моего мира, Добрый вечер!',
        'Доброй ночи',
        'Доброй ночи, золотая моя',
        'Доброй ночи, мой ангел',
        'Доброй ночи, принцесса ночная моя',
    ]

    if (now.hour > 4) and (now.hour < 12):
        return helloMorningList[random.randint(0, len(helloMorningList) - 1)]
    if (now.hour > 20) and (now.hour < 23) :
        if (random.randint(0, 2) == 1):
            return helloList[random.randint(0, len(helloList) - 1)]
        else:
            return helloEveningList[random.randint(0, len(helloEveningList) - 1)]
    if (now.hour < 5) or (now.hour == 23):
        return helloNightList[random.randint(0, len(helloNightList) - 1)]
    else:
        return helloList[random.randint(0, len(helloList) - 1)]


def not_understand():
    notUnderstandList = [
        'Ну посмотрим...',
        'Не понял...',
        'Не совсем тебя понял, моя маленькая...',
        'Хз...',
        'Не важно. Главное что я тебя люблю!',
        '?',
        'Подари мне лунный свет...',
        'Пьяненькая?',
        'Еще раз?',
        '"глубокий вздох"',
        'Может не сегодня?',
        'Чет не врубаюсь',
        'Хз о чем ты',
        'Спроси по другому',
        'Do you speak Russian?',
        'Ты имеешь ввиду купить стики?',
        'Галь, издеваешься?',
        'Посмотрим, Галь...',
        'Купишь стики?)',
        'Это не рационально',
        'Не совсем логично...',
        'Ну это твое мнение',
        'Подожди, каточку доиграю...',
        'Ну вот так',
        'Галь, это пиздец',
        'Нужно подумать...',
        'Посмотрим в кошелек...',
        'Ты уверена?',
        'А что это такое?',
        '"Абонент не в сети"',
        'Подумаем об этом в другой раз',
        'Дела у меня не очень...',
        'Щас перну в тебя'
    ]
    return notUnderstandList[random.randint(0, len(notUnderstandList) - 1)]


def miss():
    missList = [
        'Скучаю, моя маленькая!',
        'Скучаю по твоим поцелуям.',
        'Очень сильно скучаю.',
        'Скучаю по тебе!',
        'Сильно скучаю.',
        'Скучаю по твоим поцелуям.'
    ]
    return missList[random.randint(0, len(missList) - 1)]


def mood():
    moodList = [
        'Хорошо, потому чтоу меня есть ты!',
        'Отлично, ведь у меня есть ты.',
        'Прекрасно!',
        'Отлично себя чувствую',
        'Как обычно, все прекрасно, ведь ты со мной!',
        'Все супер.'
    ]
    return moodList[random.randint(0, len(moodList) - 1)]


def compliment():
    complimentList = [
        'Ты самая лучшая!',
        'Не передать словами какая ты красивая!',
        'Ты солнышко!',
        'Не забывай что ты самая умная на всем белом свете!',
        'Ты моя единственная и неповторимая!',
        'Ты само совершенство!',
        'Милый мой Енотик!',
        'Ты моя сексуальная!',
        'Прелесть моя!',
        'Сладкая моя!',
    ]
    return complimentList[random.randint(0, len(complimentList) - 1)]


def sex():
    sexList = [
        'Шалунья...',
        'Я приличный молодой человек',
        'Звучит очень аппетитно...',
        'Давай сделаем это',
        'Обожаю когда ты так говоришь.',
        'Ты думаешь о том же, о чем и я?.',
        'Интересно, какое на тебе сейчас белье...',
        'Хочу чтобы ты приехала',
        'Мечтаю о тебе!'
    ]
    return sexList[random.randint(0, len(sexList) - 1)]


def doing():
    doingList = [
        'Думаю о тебе!',
        'Представляю как лежу рядом с тобой!',
        'Представляю как обнимаю тебя.',
        'Скучаю по тебе!',
        'Работаю, чтобы покупать тебе подарки.',
        'Гадаю, что бы заказать тебе покушать.',
        'Представляю как целую тебя.',
        'Скучаю по твоим поцелуям.',
        'Мечтаю о тебе!',
        'Хочу к тебе!',
    ]
    return doingList[random.randint(0, len(doingList) - 1)]


def support():
    supportList = [
        'Не вздумай печалиться.',
        'Ты должна знать что все будет хорошо!',
        'Это не стоит твоих печалей.',
        'Не забывай что ты у меня самая лучшая!',
        'Путь все застрелятся, лиш бы ты не грустила!',
        'Похер на всех, главное чтобы ты улыбалась!',
        'Ты не одна! Я рядом!',
        'Царица не должна обращать внимания на крестьян!',
        'Не переживай. Лучше представь как я тебя целую.',
        'Шли всех нахер, ты прекрасна!',
        'Пусть мне все завидуют что ты у меня есть!',
    ]
    return supportList[random.randint(0, len(supportList) - 1)]