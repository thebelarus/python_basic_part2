import math


def is_coin_in_circle(coordinate_x, coordinate_y, radius) -> bool:
    '''Поиск нахождения точки в круге.

    Возврат тип bool.
    '''
    length = math.sqrt(coordinate_x**2 + coordinate_y**2)
    if length <= radius:
        return True
    return False


if __name__ == '__main__':
    print('Введите координаты монетки:')
    coordinate_x_input = float(input('X: '))
    coordinate_y_input = float(input('Y: '))
    radius_input = float(input('Введите радиус: '))
    coin_found_status = is_coin_in_circle(
        coordinate_x_input,
        coordinate_y_input,
        radius_input
    )
    if coin_found_status:
        print('Монетка где-то рядом.')
    else:
        print('Монетки в области нет.')

# TODO применить рекомендации данные ранее
