def calculate_straight_line_equation(x1, y1, x2, y2) -> str:
    """Нахождение уравнения прямой."""
    x_diff = x1 - x2
    y_diff = y1 - y2
    if x_diff == 0:
        return f"x = {x1}"
    elif y_diff == 0:
        return f"y = {y1}"
    else:
        k = y_diff / x_diff
        b = y2 - k * x2
        return f"y = , {k},  * x + , {b}"


if __name__ == '__main__':
    print("Введите первую точку")
    x1_input = float(input('X: '))
    y1_input = float(input('Y: '))
    print("\nВведите вторую точку")
    x2_input = float(input('X: '))
    y2_input = float(input('Y: '))
    straight_line_equation = calculate_straight_line_equation(
        x1_input,
        y1_input,
        x2_input,
        y2_input
    )
    print("Уравнение прямой, проходящей через эти точки:")
    print(straight_line_equation)

# зачет!
