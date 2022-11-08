def code_string(string):
    if not string:
        return string
    result_string = ''
    curent_symbol = string[0]
    symbol_counter = 0
    for symbol in string:
        if symbol == curent_symbol:
            symbol_counter += 1
        else:
            result_string = f'{result_string}{curent_symbol}{symbol_counter}'
            curent_symbol = symbol
            symbol_counter = 1
    result_string = f'{result_string}{curent_symbol}{symbol_counter}'
    return result_string


if __name__ == '__main__':
    password_input = input('Введите строку: ')
    coded_sting = code_string(password_input)
    print(f'Закодированная строка: {coded_sting}')
