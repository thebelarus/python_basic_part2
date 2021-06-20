def generate_even_names_l(names_l) -> list:
    return names_l[::2]


if __name__ == '__main__':
    names = [
        'Артемий', 'Борис', 'Влад', 'Гоша',
        'Дима', 'Евгений', 'Женя', 'Захар'
    ]
    print(generate_even_names_l(names))

# TODO применить рекомендации данные ранее
