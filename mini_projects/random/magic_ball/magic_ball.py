from random import *

def is_valid(question):
    question = question.rstrip()
    if question[-1] == '?':
        return True
    else:
        return False

def answer(question):
    answers = [
    'Бесспорно',
    'Предрешено',
    'Никаких сомнений',
    'Определённо да',
    'Можешь быть уверен в этом',
    'Мне кажется - да',
    'Вероятнее всего',
    'Хорошие перспективы',
    'Знаки говорят - да',
    'Да',
    'Пока неясно, попробуй снова',
    'Спроси позже',
    'Лучше не рассказывать',
    'Сейчас нельзя предсказать',
    'Сконцентрируйся и спроси опять',
    'Даже не думай',
    'Мой ответ - нет',
    'По моим данным - нет',
    'Перспективы не очень хорошие',
    'Весьма сомнительно'
    ]
    if is_valid(question):
        print(choice(answers))
        return again(input('Хочешь задать еще вопрос? Напиши Да/Нет '))
    else:
        while is_valid(question) == False:
            question = input('Нужно написать вопрос ')
        answer(question)

def again(answer_again_replace):
    if answer_again_replace in ['Да', 'да']:
        answer()
    elif answer_again_replace in ['Нет', 'нет']:
        print('Возвращайся, если будут еще вопросы! ')
    else:
        while answer_again_replace not in ['Да', 'да', 'Нет', 'нет']:
            answer_again_replace = input('Необходимо ввести Да/Нет ')
        again(answer_again_replace)

def is_valid_name(name):
    if isinstance(name, str) and 1 < len(name) < 10:
        return True
    else:
        return False

name = input('Введите свое имя: ')

if is_valid_name(name):
    print(f'Привет, {name}, я магический шар, и я заню ответ на любой твой вопрос.')
else:
    while is_valid_name(name) == False:
        print('Необходимо ввести имя')
        name = input('Введите свое имя: ')
    print(f'Привет, {name}, я магический шар, ия  знаю ответ на любой твой вопрос.')

answer(input('Введите свой вопрос: '))