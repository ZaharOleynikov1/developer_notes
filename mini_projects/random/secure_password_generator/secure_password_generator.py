import random

def digit_valid(digit):
    while not digit.isdigit() or int(digit) < 1:
        digit = input('Необходимо ввести число не меньше 1 ')
    return int(digit)

def answer_valid(answer):
    while answer not in ['Да', 'да', 'Нет', 'нет']:
        answer = input('Необходимо ввести Да/Нет ')
    if answer in ['Да', 'да']:
        return 'Да'
    else:
        return 'Нет'

def generate_password(length, chars):
    password = list()
    for i in range(len(select_chars)):
        password.append(random.choice(select_chars[i]))
    for i in range(length - len(select_chars)):
        password.append(random.choice(chars))
    random.shuffle(password)
    return ''.join(password)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
select_chars = list()
number_password = digit_valid(input('Какое количество паролей необходимо сгенерировать? Введите число не меньше 1 '))
length_password = input('Какая должна быть длина одного пароля? ')

while not length_password.isdigit() or int(length_password) < 4:
    length_password = input('Пароль меньше 4 символом слишком небезопасен. Введите число не меньше 4 ' )
length_password = int(length_password)

if answer_valid(input('Включать ли цифры "0123456789"? Введите Да/Нет ')) == 'Да':
    select_chars.append(digits)
    chars += digits

if answer_valid(input('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? Введите Да/Нет ')) == 'Да':
    select_chars.append(uppercase_letters)
    chars += uppercase_letters

if answer_valid(input('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"? Введите Да/Нет ')) == 'Да':
    select_chars.append(lowercase_letters)
    chars += lowercase_letters

if answer_valid(input('Включать ли символы "!#$%&*+-=?@^_"? Введите Да/Нет ')) == 'Да':
    select_chars.append(punctuation)
    chars += punctuation

if answer_valid(input('Исключать ли неоднозначные символы "il1Lo0O"? Введите Да/Нет ')) == 'Да':
    for i in 'il1Lo0O':
        if i in chars:
            chars = chars.replace(i, '')
    for i in range(0, len(select_chars)):
        for j in 'il1Lo0O':
            if j in select_chars[i]:
                select_chars[i] = select_chars[i].replace(j, '')

if not chars:
    print('Необходимо выбрать хотябы один набор символов' )
else:
    for i in range(number_password):
        print(generate_password(length_password, chars))