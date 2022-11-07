# Задача 2. Самое длинное слово
# Что нужно сделать
# Пользователь вводит строку, содержащую пробелы.
# Найдите в ней самое длинное слово, выведите это слово и его длину.
# Если таких слов несколько, выведите первое из них.
def get_max_word(string):
    splited_string = string.split()
    if not splited_string:
        return '', 0
    result = max(splited_string, key=lambda word: len(word))
    return result, len(result)


if __name__ == '__main__':
    string_input = input('Доступное меню: ')
    max_word, max_word_length = get_max_word(string_input)
    print(f'Самое длинное слово: {max_word}')
    print(f'Длина этого слова: {max_word_length}')
