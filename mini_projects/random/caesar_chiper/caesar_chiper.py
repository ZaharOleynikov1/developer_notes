RU_LOWER = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
RU_UPPER = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

EN_LOWER = 'abcdefghijklmnopqrstuvwxyz'
EN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text_list = list()


def alphabet_valid(alphabet):
    while alphabet not in ['Ru', 'ru', 'En', 'en']:
        alphabet = input(
            'Необходимо ввести Ru/En'
        )

    if alphabet in ['Ru', 'ru']:
        return 'Ru'
    else:
        return 'En'


def shift_valid(shift):
    while not shift.isdigit() or int(shift) < 0:
        shift = input(
            'Необходимо ввести число не меньше 0'
        )

    return int(shift)


def text_valid(text):
    for i in text:
        while i in ['Ё', 'ё']:
            text = input(
                'В введеном тексте есть буква "ё", замените данную букву на "е"'
            )
    
    if alphabet == 'Ru':
        for i in text:
            while i not in RU_UPPER or i not in RU_LOWER:
                text = input(
                    'В введеном тексте есть буквы из английского алфавита'
                )

        return text

    if alphabet == 'En':
        for i in text:
            while i not in EN_LOWER or i not in EN_UPPER:
                text = input(
                    'В введеном тексте есть буквы из русского алфавита'
                )

            return text
                

direction = input(
    'Выберете, шифрование или дешифрование'
)

while direction not in ['Шифрование', 'шифрование', 'Дешифрование', 'дешифрование']:
    direction = input(
        'Необходимо ввести Шифрование/Дешифрование'
    )

if direction in ['Шифрование', 'шифрование', 'Дешифрование', 'дешифрование']:
    alphabet = alphabet_valid(
        input(
            'Выберете алфавит. Введите Ru/En'
    )
)
    shift = shift_valid(
        input(
            'Введите количество сдвига'
    )
)
    text = text_valid(
        input(
            'Введите текст, который нужно зашифровать'
    )
)
    if direction in ['Шифрование', 'шифрование']:
        if alphabet in ['Ru', 'ru']:
            for i in text:
                if i.isupper():
                    text_list.append(RU_UPPER[(RU_UPPER.index(i) + shift) % len(RU_LOWER)])
                elif i.islower():
                    text_list.append(RU_LOWER[(RU_LOWER.index(i) + shift) % len(RU_LOWER)])
                else:
                    text_list.append(i)
            print(''.join(text_list))
        else:
            for i in text:
                if i.isupper():
                    text_list.append(EN_UPPER[(EN_UPPER.index(i) + shift) % len(EN_LOWER)])
                elif i.islower():
                    text_list.append(EN_LOWER[(EN_LOWER.index(i) + shift) % len(EN_LOWER)])
                else:
                    text_list.append(i)
            print(''.join(text_list))
    else:
        if alphabet in ['Ru', 'ru']:
            for i in text:
                if i.isupper():
                    text_list.append(RU_UPPER[(RU_UPPER.index(i) - shift) % len(RU_LOWER)])
                elif i.islower():
                    text_list.append(RU_LOWER[(RU_LOWER.index(i) - shift) % len(RU_LOWER)])
                else:
                    text_list.append(i)
            print(''.join(text_list))
        else:
            for i in text:
                if i.isupper():
                    text_list.append(EN_UPPER[(EN_UPPER.index(i) - shift) % len(EN_LOWER)])
                elif i.islower():
                    text_list.append(EN_LOWER[(EN_LOWER.index(i) - shift) % len(EN_LOWER)])
                else:
                    text_list.append(i)
            print(''.join(text_list))
    
