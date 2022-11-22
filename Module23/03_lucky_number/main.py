import random


def write_to_file(data, filename='out_file.txt'):
    with open(filename, 'a', encoding='utf8') as file:
        file.write(f'{data}\n')


def get_random_number():
    return random.randint(1, 13)


def main():
    amount = 0
    try:
        while amount < 777:
            try:
                number_input = int(input('Введите число: '))
            except ValueError as error:
                print('Вы ввели не число!')
                continue
            amount += number_input
            if get_random_number() == 1:
                raise SystemExit('Вас постигла неудача!')
            write_to_file(number_input)
    except SystemExit as error:
        print(error)
        raise SystemExit
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')


if __name__ == '__main__':
    main()
