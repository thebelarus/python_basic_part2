def number_generator(array_range):
    return [1 if number % 2 == 0 else number % 5
            for number in range(array_range)]


if __name__ == '__main__':
    array_length = int(input('Введите длину списка: '))
    result = number_generator(array_length)
    print(f'Результат: {result}')
