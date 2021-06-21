
def generate_videocards(videocards_count) -> list:
    if not isinstance(videocards_count, int):
        raise ValueError('Требуется целое число!')
    result = []
    for index in range(videocards_count):
        value_input = int(input(f'{index+1} Видеокарта: '))
        result.append(value_input)
    return result


def filter_videocards(videocards) -> list:
    if not isinstance(videocards, list):
        raise ValueError('Требуется список!')
    result = [
        videocard for videocard in videocards if videocard != max(videocards)
    ]
    return result


if __name__ == '__main__':
    videocards_count_input = int(input('Кол-во видеокарт: '))
    videocards_input = generate_videocards(videocards_count_input)
    print(f'Старый список видеокарт: {videocards_input}')
    videocards_input = filter_videocards(videocards_input)
    print(f'Новый список видеокарт: {videocards_input}')
