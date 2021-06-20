def count_position(containers_l, value):
    if not isinstance(containers_l, list):
        raise ValueError('Требуется список контейнеров!')
    if not isinstance(value, int):
        raise ValueError('Требуется целое число массы контейнера!')
    cont_bigger_than_value = [x for x in containers_l if x >= value]
    return len(cont_bigger_than_value) + 1


if __name__ == '__main__':
    containers_count = int(input('Кол-во контейнеров: '))
    containers_l_input = []
    for _ in range(containers_count):
        corect_input_status = False
        while(not corect_input_status):
            try:
                container_value = int(input('Введите вес контейнера: '))
                if container_value > 200:
                    print('Ошибка! Масса не должна превышать 200кг.')
                else:
                    containers_l_input.append(container_value)
                    corect_input_status = True
            except ValueError:
                print('Ошибка! Масса должна быть целым числом!')

    corect_input_status = False
    new_container_value = 0
    while(not corect_input_status):
        new_container_value = int(input('Введите вес нового контейнера: '))
        if new_container_value > 200:
            print('Ошибка! Масса не должна превышать 200кг.')
        else:
            corect_input_status = True
    new_postion = count_position(containers_l_input, new_container_value)
    print(f'Номер, куда встанет новый контейнер: {new_postion}')

# TODO применить рекомендации данные ранее
