import random
from datetime import datetime


def get_menu():
    return '1. Посмотреть текущий текст чата.\n'\
        '2. Отправить сообщение(затем вводит сообщение).'


def read_chat_base(filename='chat.txt'):
    try:
        with open(filename, encoding='utf8') as file:
            return file.readlines()
    except FileNotFoundError as error:
        return []


def write_to_chat_base(user, text, filename='chat.txt'):
    try:
        with open(filename, 'a', encoding='utf8') as file:
            record_datetime = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
            file.write(f'{record_datetime} ({user}) - {text}\n')
    except Exception as error:
        return False, error
    else:
        return True, 'Cообщение записано'


def main():
    username = input('Введите веше имя пользователя: ')
    while True:
        print(get_menu())
        try:
            menu_select = int(input('Ваш выбор: '))
            if menu_select not in [1, 2]:
                raise ValueError
        except ValueError:
            print('Введите число из меню!')
            continue
        if menu_select == 1:
            chat = read_chat_base()
            if chat:
                for row in chat:
                    print(row, end='')
            else:
                print('Чат пуст.')
        elif menu_select == 2:
            chat = read_chat_base()
            message_text = input('Введите сообщение: ')
            _, message = write_to_chat_base(username, message_text)
            print(message)


if __name__ == '__main__':
    main()
