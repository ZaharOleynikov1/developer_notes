from random import *

def is_valid(digit):
    if digit.isdigit() and 1 <= int(digit) <= 100:
        return True
    else:
        return False

def is_limit():
    text_variations = [
        'А может все-таки введем число от 1 до 100?',
        'Математика намекает: число должно быть от 1 до 100!',
        'Попытка засчитана... шучу =). Введите число от 1 до 100!'            
        ]
    random = randint(0, len(text_variations) - 1)
    return text_variations[random]

digit_random = randint(1, 100)

print('Добро пожаловать в числовую угадайку!')
print()
print('Для начала игры, выберете, какое число будет пределом игрового диапазона.')
print()
print('Пример: при вводе числа 100, программа загадает число от 1 до 100')
print('Ваша задача отгадать загаданое число программой и при этом затратить как можно меньше попыток на поиск. Игра началась!')

flag = False
counter = 0

while flag == False:
    digit = input()
    if is_valid(digit):
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
    else:
        print(is_limit())