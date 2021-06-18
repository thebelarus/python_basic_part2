def calculate_straight_line_odds(x1, y1, x2, y2) -> tuple:
    '''  # TODO аменить на """ """
    Вычисление углового коэффициента и вертикального смещения.

    Возвращает кортеж (k, b), где:
    k : угловой коэффициент прямой,
    b : вертикальное смещение прямой.
    В случае признака параллельности осям, вызывается исключение.
    '''
    x_diff = x1 - x2
    y_diff = y1 - y2
    if x_diff == 0 or y_diff == 0:
        raise ValueError(
            'Данная прямая параллельна оси Ox(Oy).'
            'Для такой прямой угловой коэффициент'
            ' и вертикальное смещение прямой не существует.'
            )
    k = y_diff / x_diff
    b = y2 - k * x2
    return k, b


if __name__ == '__main__':
    print("Введите первую точку")
    x1 = float(input('X: '))
    y1 = float(input('Y: '))
    print("\nВведите вторую точку")
    x2 = float(input('X: '))
    y2 = float(input('Y: '))
    try:
        k, b = calculate_straight_line_odds(x1, y1, x2, y2)
        print("Уравнение прямой, проходящей через эти точки:")
        print("y = ", k, " * x + ", b)
    except ValueError as error:
        print(error)

# TODO нужно делать уонструкцию вида if elif else
# TODO где в первых двух будем обработка если x_diff = 0 во втором y_diff = 0
# TODO при входных данных 10 20 и 10 45 ответ x = 10.0


# Начиная с этого модуля буду обращать внимание на то что подчеркивает Пайчар. Придерживаемся PEP8
# Можно привести все к нужному формату code\Reformat code

# TODO Есть недочеты в форматировании по PEP8, используйте пункт меню в пайчарме
