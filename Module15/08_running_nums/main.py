def shift_table(table_l, k_value) -> None:
    for index in range(k_value):
        table_l = table_l[-1:] + table_l[:-1]
        print(f'Cдвиг {index+1}: {table_l}')


if __name__ == '__main__':
    n = [1, 4, -3, 0, 10]
    k = 5
    print(f'Изначальный список: {n}')
    shift_table(n, k)
    print(f'Сдвинутый список: {n}')
