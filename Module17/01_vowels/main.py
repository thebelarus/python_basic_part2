def vowels_parser(string):
    VOWELS = 'ауоиэыяюеё'
    return [char for char in string if char in VOWELS]


if __name__ == '__main__':
    text_input = input('Введите текст: ')
    result = vowels_parser(text_input)
    result_length = len(result)
    print(f'Список гласных букв: {result}')
    print(f'Длина списка: {result_length}')
