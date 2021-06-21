
def generate_cells(cell_count) -> list:
    if not isinstance(cell_count, int):
        raise ValueError('Требуется целое число!')
    cells = []
    for index in range(cell_count):
        value_input = int(input(f'Эффективность {index+1} клетки: '))
        cells.append(value_input)
    return cells


def filter_cells(cells) -> list:
    if not isinstance(cells, list):
        raise ValueError('Требуется список!')
    return [value for index, value in enumerate(cells) if value < index]


if __name__ == '__main__':
    cell_count_input = int(input('Кол-во клеток: '))
    generated_cells = generate_cells(cell_count_input)
    filtered_cells = filter_cells(generated_cells)
    result = ' '.join([str(item) for item in filtered_cells])
    print(f'Неподходящие значения: {result}')
