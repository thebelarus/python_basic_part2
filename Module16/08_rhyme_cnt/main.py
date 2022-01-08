"""Task 8 solution."""
if __name__ == '__main__':
    try:
        gamers_count = int(input('Кол-во человек: '))
        game_number = int(input('Какое число в считалке? '))
    except ValueError:
        print('Ошибка! Кол-во человек и число\
            в считалке должны быть целыми числами!')
    start_point = 1
    gamer_array = list(range(1, gamers_count + 1))
    while(len(gamer_array) != 1):
        print(f'Текущий круг людей: {gamer_array}')
        gamer_array_length = len(gamer_array)
        if start_point > gamer_array_length:
            start_point = start_point - gamer_array_length
        print(f'Начало счёта с номера {gamer_array[start_point-1]}')
        start_point = start_point + game_number - 1
        start_point -= gamer_array_length * (game_number // gamer_array_length)
        print(f'Выбывает человек под номером {gamer_array[start_point-1]}\n')
        del gamer_array[start_point-1]
    last_gamer = gamer_array.pop()
    print(f'Остался человек под номером {last_gamer}')
