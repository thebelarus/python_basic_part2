def print_number_in_recursion(number, storage=1):
    print(storage)
    if storage != number:
        return print_number_in_recursion(number, storage + 1)


def main():
    number_input = int(input('Введите num: '))
    print_number_in_recursion(number_input)


if __name__ == '__main__':
    main()
