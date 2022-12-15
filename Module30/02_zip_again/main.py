def main() -> None:
    '''Tестирование кода'''
    letters = ['a', 'b', 'c', 'd', 'e']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    results = list(map(lambda value_one, value_two: (
        value_one, value_two), letters, numbers))
    print('Результат работы программы:')
    print(results)


if __name__ == '__main__':
    main()
