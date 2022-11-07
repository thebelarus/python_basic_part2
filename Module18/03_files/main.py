def validate_filename(filename):
    FORBIDDEN_SYMBOLS = '@№$% ^ &\\*()'
    ALLOWED_EXTENSIONS = ['.txt', '.docx']
    if not [True for extension in ALLOWED_EXTENSIONS
            if filename.endswith(extension)]:
        extenstion_string = ' или '.join(ALLOWED_EXTENSIONS)
        return False, 'Ошибка: неверное расширение файла. '\
            f'Ожидалось {extenstion_string}.'
    if [True for extension in FORBIDDEN_SYMBOLS
            if filename.startswith(extension)]:
        return False, 'Ошибка: название начинается на'\
            'один из специальных символов.'
    return True, 'Файл назван верно.'


if __name__ == '__main__':
    filename_input = input('Название файла: ')
    _, result_message = validate_filename(filename_input)
    print(result_message)
