"""Task 10 solution."""
if __name__ == '__main__':
    number_array = []
    try:
        number_count = int(input('Кол-во чисел: '))
        for _ in range(number_count):
            number_array.append(int(input('Число: ')))
    except ValueError:
        print('Ошибка! Допускаются для ввода только целые числа!')

    number_string = ' '.join([str(item) for item in number_array])
    print(f'Последовательность: {number_string}')
    number_needed = 0
    number_array_len = len(number_array)
    needed_numbers_array = []
    for index in range(number_array_len):
        first_element = number_array[number_array_len-index-2]
        last_element = number_array[number_array_len-index-1]
        if first_element != last_element:
            number_needed += 1
            needed_numbers_array.append(first_element)
            number_array.append(first_element)

    needed_string = ' '.join([str(item) for item in needed_numbers_array])
    print(f'Нужно приписать чисел: {number_needed}')
    print(f'Сами числа: {needed_string}')
