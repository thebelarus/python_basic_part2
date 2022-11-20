import os


def construct_path(dirs):
    array = []
    if os.name == 'nt':
        array.append('C:\\')
    array.extend(dirs.split())
    return os.path.join(*array)


def is_path_exists(path):
    if os.path.exists(path):
        return True
    return False


def is_file_exists(path, filename):
    filepath = os.path.join(path, filename)
    if os.path.exists(filepath):
        return True
    return False


def write_to_file(path_value, filename_value, data_value):
    with open(
        os.path.join(path_value, filename_value),
        'w',
        encoding='utf8'
    ) as file:
        file.write(data_value)


def write_data_to_path(path, filename, data):
    if is_path_exists(path):
        is_file_exists_status = is_file_exists(path, filename)
        if is_file_exists_status:
            user_input = input('Вы действительно хотите перезаписать файл? ')
            if user_input == 'да':
                write_to_file(path, filename, data)
                return True, 'Файл успешно перезаписан!'
            else:
                return False, 'Файл не перезаписан!'
        write_to_file(path, filename, data)
        return True, 'Файл успешно сохранён!'
    return False, 'Данного пути не существует!'


def is_txt_filename_extenstion(filename):
    if filename[-4:] == '.txt' and len(filename) > 4:
        return True
    return False


def main():
    text_input = input('Введите строку: ')
    dirs_input = input('Куда хотите сохранить документ?\
        Введите последовательность папок(через пробел): ')
    filename_input = input('Введите имя файла: ')
    if is_txt_filename_extenstion(filename_input):
        constructed_path = construct_path(dirs_input)
        _, message = write_data_to_path(
            constructed_path,
            filename_input,
            text_input
        )
        print(message)
    else:
        print('Расширение файла не .txt или имя файла не действительно!')


if __name__ == '__main__':
    main()
