def count_unique_letters(word):
    if not isinstance(word, str):
        raise ValueError('Требуется список!')
    unique_letters_counter = 0
    for letter in word:
        if list(word).count(letter) == 1:
            unique_letters_counter += 1
    return unique_letters_counter


if __name__ == '__main__':
    word_input = input('Введите слово: ')
    unique_letters_count = count_unique_letters(word_input)
    print(f'Кол-во уникальных букв: {unique_letters_count}')


# зачет!
