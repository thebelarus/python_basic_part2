def is_possible_palindrome(string):
    storage = {}
    for symbol in string:
        if symbol not in storage:
            storage[symbol] = 1
        else:
            storage[symbol] += 1
    if len(
        {
            (symbol, count) for (symbol, count)
            in storage.items() if count % 2 != 0
        }
    ) >= 2:
        return False
    return True


if __name__ == '__main__':
    input_string = input('Введите строку: ')
    result = is_possible_palindrome(input_string)
    if result:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')
