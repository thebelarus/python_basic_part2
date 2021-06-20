
def generate_cells_l(cell_count) -> list:
    if not isinstance(cell_count, int):
        raise ValueError('Требуется целое число!')
    result_l = []
    for index in range(cell_count):
        value_input = int(input(f'Эффективность {index+1} клетки: '))
        result_l.append(value_input)
    return result_l


def filter_cells_l(cells_l) -> list:
    if not isinstance(cells_l, list):
        raise ValueError('Требуется список!')
    return [value for index, value in enumerate(cells_l) if value < index]


if __name__ == '__main__':
    cell_count_input = int(input('Кол-во клеток: '))
    generated_cells_l = generate_cells_l(cell_count_input)
    filtered_cells_l = filter_cells_l(generated_cells_l)
    result = ' '.join([str(item) for item in filtered_cells_l])
    print(f'Неподходящие значения: {result}')

# TODO применить рекомендации данные ранее
