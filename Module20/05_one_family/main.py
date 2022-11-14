people = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,
    'Иванов Никита': 25,
    'Иванова Алина': 24,
    'Иванов Павел': 1,
}


def search_by_last_name(base, last_name):
    return [
        f'{key} {value}' for key, value in base.items()
        if last_name.lower() in key.lower()
    ]


def main():
    last_name_input = input('Введите фамилию: ')
    result = search_by_last_name(people, last_name_input)
    for item in result:
        print(item)


if __name__ == '__main__':
    main()
