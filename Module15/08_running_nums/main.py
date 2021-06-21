def shift_table(table, shift) -> None:
    for index in range(shift):
        table = table[-1:] + table[:-1]
        print(f'Cдвиг {index+1}: {table}')


if __name__ == '__main__':
    n = [1, 4, -3, 0, 10]
    k = 5
    print(f'Изначальный список: {n}')
    shift_table(n, k)
    print(f'Сдвинутый список: {n}')
