import zipfile


def get_sorted_analysis_base(base):
    total_chars = sum(base.values())
    stats = [(k, round((v / total_chars), 6)) for k, v in base.items()]
    result = sorted(stats, key=(lambda item: (-item[1], item[0])))
    return result


def main():
    zip_filename = 'voyna-i-mir.zip'
    txt_filename = 'voyna-i-mir.txt'
    base = {}
    with zipfile.ZipFile(zip_filename) as zip_file:
        with zip_file.open(txt_filename) as file:
            for char in file.read().decode('utf-8'):
                if char.isalpha():
                    if char in base:
                        base[char] += 1
                    else:
                        base[char] = 1
    result = get_sorted_analysis_base(base)
    for item in result:
        print(f'{item[0]} {item[1]:.9f}')


if __name__ == '__main__':
    main()
