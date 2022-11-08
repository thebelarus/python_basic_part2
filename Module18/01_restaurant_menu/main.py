def convert_menu(menu):
    return ', '.join(menu.split(';'))


if __name__ == '__main__':
    menu_input = input('Доступное меню: ')
    result = convert_menu(menu_input)
    if result:
        print(f'На данный момент в меню есть: {result}')
    else:
        print('На данный момент в меню пусто')
