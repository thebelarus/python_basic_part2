def is_palindrome(word):
    if not isinstance(word, str):
        raise ValueError('Ошибка! Требуется строка!')
    if word == word[::-1]:
        return True
    return False


if __name__ == '__main__':
    word_input = input('Кол-во контейнеров: ')
    if is_palindrome(word_input):
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')

# зачет!
