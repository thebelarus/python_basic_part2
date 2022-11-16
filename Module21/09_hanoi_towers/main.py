def hanoi_tower(number, stick_1='1', stick_2='2', stick_3='3'):
    temp_number = 0
    if number == 1:
        print(
            f'Переложить диск {number} со стержня номер \
                {stick_1} на стержень номер {stick_3}')
        temp_number = 1
    else:
        temp_number = hanoi_tower(
            number - 1,
            stick_1='1',
            stick_2='3',
            stick_3='2'
            )
        print(
            f'Переложить диск {number} со стержня номер \
                {stick_1} на стержень номер {stick_3}')
        temp_number += 1
        temp_number += hanoi_tower(
            number - 1,
            stick_1='2',
            stick_2='1',
            stick_3='3'
            )
    return temp_number


def main():
    hanoi_tower(2)


if __name__ == '__main__':
    main()
