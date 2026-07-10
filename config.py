COLOR_DARK = '#0d0a0c'
COLOR_LIME = '#99ff66'
COLOR_BLACK = '#000000'
COLOR_WHITE = '#ffffff'
COLOR_RED = 'red'

FONT_LARGE = ('Constantia', 30)
FONT_MEDIUM = ('Constantia', 25)
FONT_SMALL = ('Constantia', 20)

BTN_PARAMS = {
    "height": 50,
    "corner_radius": 50,
    "fg_color": COLOR_LIME,
    "hover_color": COLOR_WHITE,
    "text_color": COLOR_BLACK,
    "font": ('Constantia', 20)
}

BOX_PARAMS = {
    "font": ('Calibri', 23),
    "text_color": COLOR_WHITE,
    "fg_color": COLOR_WHITE,
    "border_color": COLOR_WHITE,
    "hover_color": COLOR_LIME,
    "text_color_disabled": COLOR_WHITE,
    "border_width_checked": 5,
    "border_width_unchecked": 1
}

STATIC_PAGES_DATA = {
    'GreetingsPage': {
        'labels': [
            ('Приветствую!', COLOR_WHITE, FONT_LARGE, 0.5, 0.3),
            ('Это - игра "Викторина"', COLOR_LIME, FONT_LARGE, 0.5, 0.45),
            ('Сыграем?', COLOR_WHITE, FONT_LARGE, 0.5, 0.6)
        ],
        'buttons': [
            ('Не сейчас', 'exit', 0.35, 0.8),
            ('Давай!', 'next', 0.65, 0.8),
        ]
    },
    'RulesPage': {
        'labels': [
            ('Правила очень просты:', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.1),
            ('Я задам тебе несколько вопросов', COLOR_LIME, FONT_MEDIUM, 0.5, 0.2),
            ('на самые разные темы', COLOR_WHITE, FONT_LARGE, 0.5, 0.3),
            ('а тебе нужно выбрать правильный ответ', COLOR_LIME, FONT_MEDIUM, 0.5, 0.4),
            ('за каждый из которых', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.5),
            ('тебе начисляется балл', COLOR_LIME, FONT_MEDIUM, 0.5, 0.6),
            ('По итогу: считаем баллы', COLOR_WHITE, FONT_MEDIUM, 0.5, 0.7),
            ('Начнём?', COLOR_LIME, FONT_MEDIUM, 0.5, 0.8)
        ],
        'buttons': [
            ('Выйти', 'exit', 0.35, 0.92),
            ('Начнём', 'start', 0.65, 0.92)
        ]
    }
}

QUIZ_PAGE_DATA = {
    'frames': [
        ('question_frame', COLOR_DARK, 0, 0.2, 1.0, 0.3),
        ('answer_frame', COLOR_DARK, 0, 0.5, 1.0, 0.3)
    ],
    'labels': [
        ('step_label', COLOR_LIME, FONT_MEDIUM, 0.25, 0.1),
        ('score_label', COLOR_WHITE, FONT_MEDIUM, 0.7, 0.1),
        ('comment_label', COLOR_LIME, FONT_MEDIUM, 0.5, 0.9)
    ],
    'buttons': [
        ('Назад', 'back', 0.35, 0.9),
        ('Далее', 'next', 0.65, 0.9)
    ]
}

GAME_DATA = [
    {
        'question': 'Какая река считается самой длинной в мире?',
        'options': ['А) Амазонка', 'Б) Нил', 'В) Миссисипи'],
        'answer': 0
    },
    {
        'question': 'Какой фильм получил\n самую первую премию «Оскар»\n в номинации «Лучший фильм» в 1929 году?',
        'options': ['А) «Унесенные ветром»', 'Б) «Крылья»',  'В) «Огни большого города»'],
        'answer': 1
    },
    {
        'question': 'Какой химический элемент обозначается\n символом Fe в таблице Менделеева?',
        'options': ['А) Фтор', 'Б) Свинец', 'В) Железо'],
        'answer': 2
    },
    {
        'question': 'В каком году произошло\n падение Берлинской стены?',
        'options': ['А) 1987', 'Б) 1989', 'В) 1991'],
        'answer': 1
    },
    {
        'question': 'Какое животное способно\n развивать самую высокую\n скорость бега на короткие дистанции?',
        'options': ['А) Гепард', 'Б) Антилопа гну', 'В) Лев'],
        'answer': 0
    }
]

DELAY_MESSAGES = {
    'waiting': [
        'Жду ответа от сервера...', 'Посылаю запрос...',
        'Нужно немного подождать...', 'Дай-ка подумать...',
        'Получаю твой ответ...'
    ],
    'loading': [
        'Генерирую цикл...',
        'Создаю всё с нуля...',
        'Очищаю всё лишнее...',
        'Отлично! Начинаем...',
        'Дай мне пару секундочек!'
    ],
    'farewell': [
        'До новых встреч!',
        'Заглядывай ко мне ещё!',
        'Был рад поработать с тобой!',
        'Ты это, заходи, если что...',
        'Надеюсь, еще увидимся!'
    ]
}

GAME_MESSAGES = {
    'right': [
        'Верно!\nПравильный ответ:',
        'Отлично!\nПравильный ответ:',
        'Так держать!\nПравильный ответ:',
        'Прямо в точку\nПравильный ответ:',
        'Угадал!\nПравильный ответ:'
    ],
    'wrong': [
        'Мимо\nПравильный ответ:',
        'Не верно\nПравильный ответ:',
        'Не угадал\nПравильный ответ:',
        'Не-а\nПравильный ответ:',
        'Не то\nПравильный ответ:'
    ]
}