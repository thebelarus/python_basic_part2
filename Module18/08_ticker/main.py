def compare_offsets(for_compare, for_changes):
    for_compare_array = list(for_compare)
    array = list(for_changes)
    for attempt in range(1, len(array)+1):
        array.append(array.pop(0))
        if array == for_compare_array:
            return True, f'Первая строка получается из '\
                'второй со сдвигом {attempt}.'
    return False, 'Первую строку нельзя получить '\
        'из второй с помощью циклического сдвига.'


if __name__ == '__main__':
    first_string_input = input('Первая строка: ')
    second_string_input = input('Вторая строка: ')
    _, result = compare_offsets(first_string_input, second_string_input)
    print(result)
