def generate_even_names(names) -> list:
    return names[::2]


if __name__ == '__main__':
    name_input = [
        'Артемий', 'Борис', 'Влад', 'Гоша',
        'Дима', 'Евгений', 'Женя', 'Захар'
    ]
    result = generate_even_names(name_input)
    print(result)

# зачет!
