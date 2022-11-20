import os


def get_path_stats(path):
    files_amount = 0
    dirs_amount = 0
    total_size_bytes = 0
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            files_amount += 1
            total_size_bytes += os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            dirs_amount += 1
    total_size_kb = total_size_bytes / 1024
    return (
        files_amount,
        dirs_amount,
        total_size_kb
    )


def main():
    path_value = 'C:\\'
    files_amount, dirs_amount, total_size_kb = get_path_stats(path_value)
    print(path_value)
    print(f'Размер каталога(в Кб): {total_size_kb}')
    print(f'Количество подкаталогов: {dirs_amount}')
    print(f'Количество файлов: {files_amount}')


if __name__ == '__main__':
    main()
