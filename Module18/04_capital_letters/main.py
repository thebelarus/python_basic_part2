def normalize_string(string):
    return ' '.join([word.lower().capitalize() for word in string.split()])


if __name__ == '__main__':
    string_input = input('Введите строку: ')
    result = normalize_string(string_input)
    print(f'Результат: {result}')
