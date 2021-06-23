def shift_table(table, shift) -> None:
    for index in range(shift):
        table = table[-1:] + table[:-1]
        print(f'Cдвиг {index+1}: {table}')


if __name__ == '__main__':
    numbers = [1, 4, -3, 0, 10]
    shift_value = 5
    print(f'Изначальный список: {numbers}')
    shift_table(numbers, shift_value)
    print(f'Сдвинутый список: {numbers}')

# зачет!
