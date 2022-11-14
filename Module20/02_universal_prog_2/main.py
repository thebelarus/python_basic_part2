def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for num in range(3, int(number**0.5)+1, 2):
        if number % num == 0:
            return False
    return True


def crypto(data):
    return [
        element_velue for element_position, element_velue
        in enumerate(data) if is_prime(element_position)
    ]


def main():
    print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(crypto('О Дивный Новый мир!'))


if __name__ == '__main__':
    main()
