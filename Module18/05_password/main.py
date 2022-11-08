def is_valide_password(password):
    if len(password) < 8:
        return False
    if not [True for symbol in password if symbol.isupper()]:
        return False
    if len([True for symbol in password if symbol.isnumeric()]) < 3:
        return False
    return True


if __name__ == '__main__':
    while True:
        password_input = input('Придумайте пароль: ')
        result = is_valide_password(password_input)
        if result:
            print('Это надёжный пароль!')
            break
        print('Пароль ненадёжный. Попробуйте ещё раз.')
