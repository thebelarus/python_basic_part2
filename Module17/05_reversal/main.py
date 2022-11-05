def reverse(string):
    first_symbol_index = string.index('h') + 1
    last_symbol_index = len(string) - string[::-1].index('h') - 1
    return string[first_symbol_index:last_symbol_index][::-1]


if __name__ == '__main__':
    input_sting = input('Введите строку: ')
    result = reverse(input_sting)
    print('Развернутая последовательность '
          f'между первым и последним h: {result}')
