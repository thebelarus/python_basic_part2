def print_menu():
    print(
        'Введите номер действия:\n',
        '1. Добавить контакт\n',
        '2. Найти человека',
    )


def add_to_cotacts(contacts, phone, name):
    if name.split() != 2:
        raise ValueError('Недостаточно данных для обработки')
    first_name, last_name = name.split()
    if (first_name, last_name) in contacts:
        print('Такой человек уже есть в контактах.')
    else:
        contacts[(first_name, last_name)] = phone


def search_contact(contacts, last_name):
    return [
        f'{" ".join(name)} {phone}' for name, phone
        in contacts.items() if last_name.lower() in name[1].lower()
    ]


def main():
    my_contacts = {}
    while True:
        print_menu()
        menu_select = int(input())
        if menu_select == 1:
            try:
                name_input = input(
                    'Введите имя и фамилию нового контакта(через пробел): ')
                phone_input = input('Введите номер телефона: ')
                add_to_cotacts(my_contacts, phone_input, name_input)
                print(f'Текущий словарь контактов: {my_contacts}')
            except ValueError as error:
                print(error)
        elif menu_select == 2:
            name_input = input('Введите фамилию для поиска: ')
            print('name_input', name_input)
            result = search_contact(my_contacts, name_input)
            print(result)
            if result:
                for item in result:
                    print(item)


if __name__ == '__main__':
    main()
