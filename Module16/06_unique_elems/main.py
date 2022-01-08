"""Task 6 solution."""
if __name__ == '__main__':
    first_array = []
    second_array = []
    while(len(first_array) != 3):
        try:
            first_array.append(int(input('Введите элемент первого списка: ')))
        except ValueError:
            print('Ошибка! Введите целое число!')
    while(len(second_array) != 7):
        try:
            second_array.append(int(input('Введите элемент второго списка: ')))
        except ValueError:
            print('Ошибка! Введите целое число!')
    print(f'Первый список: {first_array}')
    print(f'Второй список: {second_array}')
    first_array.extend(second_array)
    first_array = set(first_array)
    print(f'Новый первый список с уникальными элементами: {first_array}')
