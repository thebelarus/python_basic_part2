"""Task 7 solution."""
if __name__ == '__main__':
    skates_array = []
    people_array = []
    result_count = 0
    skates_count = int(input('Кол-во коньков: '))
    while(len(skates_array) != skates_count):
        try:
            skates_array.append(
                int(input(f'Размер {len(skates_array)+1} пары: '))
            )
        except ValueError:
            print('Ошибка! Введите целое число!')

    people_count = int(input('Кол-во людей: '))
    while(len(people_array) != people_count):
        try:
            people_array.append(
                int(input(f'Размер ноги {len(people_array)+1} человека: '))
            )
        except ValueError:
            print('Ошибка! Введите целое число!')

    for people_item in people_array:
        for skate_item in skates_array:
            if skate_item >= people_item:
                result_count += 1
                skates_array.remove(skate_item)
                break
    print(f'Наибольшее кол-во людей,\
            которые могут взять ролики: {result_count}')
