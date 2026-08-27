from random import *

def is_valid(digit_limit_low, digit_limit_high,digit):
    if digit.isdigit() and digit_limit_low <= int(digit) <= digit_limit_high:
        return True
    else:
        return False

def is_limit():
    text_variations = [
        'А может все-таки введем число в верном диапазоне?',
        'Математика намекает: число должно быть в выбранном диапазоне!',
        'Попытка засчитана... шучу =). Введите число из выбранного диапазона!',
        'Выход за границы обнаружен! Возвращайтесь в выбранный диапазон!',
        'Не-а, давай придерживаться выбранного диапазона!',
        'Мимо! Попробуйте еще раз!',
        'Интересный выбор, но игра его не принимает!',
        'Давайте без экспериментов, введите число из выбранного диапазона!',
        'Система в замешательстве... Ведите число из выбранного диапазона!'            
        ]
    random = randint(0, len(text_variations) - 1)
    return text_variations[random]

def game():
    flag = False
    counter = 0
    digit_limit_low = is_limit_digit(input('Выберете, какой будет минимальный игровой диапазон - '))
    digit_limit_high = is_limit_digit(input('Отлично! А теперь введите максимальный игровой диапазон - '))
    digit_random = randint(digit_limit_low, digit_limit_high)
    print('Число загадано! Ваша задача отгадать загаданое число программой и при этом затратить минимальное количествопопыток на поиск. Игра началась!')
    while flag == False:
        digit = input()
        if is_valid(digit_limit_low, digit_limit_high, digit):
            digit = int(digit)
            counter += 1
            if digit < digit_random:
                print('Число меньше чем загаданое')
                print('--------------------------')
                print(f'Количество попыток: {counter}')
            elif digit > digit_random:
                print('Число больше чем загаданое')
                print('--------------------------')
                print(f'Количество попыток: {counter}')
            else:
                print('Поздравляем! Вы угадали число!')
                flag = True
                return game_replace()
        else:
            print(is_limit())

def is_limit_digit(digit):
    flag = False
    while flag == False:
        if digit.isdigit():
            flag = True
            return int(digit)
        else:
            digit = input('Необходимо ввести число!')

def replace(waiting):
    if waiting in ['Да', 'да']:
        print('Хорошо!')
        return game()
    elif waiting in ['Нет', 'нет']:
        print('Хорошо, спасибо за игру!')
        return True
    else:
        return False

def game_replace():
    waiting = replace(input('Хотите сыграть в игру еще раз? Напишите Да/Нет '))
    if waiting == False:
        while waiting not in ['Да', 'да', 'Нет', 'нет']:
            waiting = replace(input('Введите Да/Нет'))

print('Добро пожаловать в числовую угадайку!')
print()

game()