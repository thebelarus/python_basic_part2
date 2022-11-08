def code_message(message):
    words_array = message.split()
    result = []
    for word in words_array:
        result.append(check_word(word))
    return ' '.join(result)


def check_word(word):
    result_array = []
    temp_word = []
    for symbol in word:
        if symbol in '.!?*:,':
            result_array.append(''.join(temp_word[::-1]))
            result_array.append(symbol)
            temp_word = []
        else:
            temp_word.append(symbol)
    result_array.append(''.join(temp_word[::-1]))
    return ''.join(result_array)


if __name__ == '__main__':
    message_input = input('Сообщение: ')
    result = code_message(message_input)
    print(f'Новое сообщение: {result}')
