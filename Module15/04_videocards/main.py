
def generate_videocards_l(videocards_count) -> list:
    if not isinstance(videocards_count, int):
        raise ValueError('Требуется целое число!')
    result_l = []
    for index in range(videocards_count):
        value_input = int(input(f'{index+1} Видеокарта: '))
        result_l.append(value_input)
    return result_l


def filter_videocards_l(videocards_l) -> list:
    if not isinstance(videocards_l, list):
        raise ValueError('Требуется список!')
    result_l = [
        value for value in videocards_l if value != max(videocards_l)
    ]
    return result_l


if __name__ == '__main__':
    videocards_count_input = int(input('Кол-во видеокарт: '))
    videocards_l_input = generate_videocards_l(videocards_count_input)
    print(f'Старый список видеокарт: {videocards_l_input}')
    videocards_l_input = filter_videocards_l(videocards_l_input)
    print(f'Новый список видеокарт: {videocards_l_input}')

# TODO применить рекомендации данные ранее
