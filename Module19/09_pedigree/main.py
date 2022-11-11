def add_row_to_base(base, string):
    child, parent = string.split()
    base[child] = parent


def get_name_rate_in_base(base, name):
    counter = 0
    while True:
        if name not in base:
            break
        else:
            counter += 1
            name = base[name]
    return counter


def get_unique_names(base):
    return set(base.keys()).union(set(base.values()))


if __name__ == '__main__':
    max_number = int(input('Введите количество человек: '))
    geologic_base = {}
    for pair_number in range(1, max_number):
        while True:
            pair_input = input(f'{pair_number} пара: ')
            if len(pair_input.split()) == 2:
                add_row_to_base(geologic_base, pair_input)
                break
    unique_names = get_unique_names(geologic_base)
    print('«Высота» каждого члена семьи:')
    for name in sorted(unique_names):
        print(name, get_name_rate_in_base(geologic_base, name))
