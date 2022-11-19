import os


def is_file_exists(filename):
    filepath = os.path.join(os.getcwd(), filename)
    if os.path.exists(filepath):
        return True
    return False


def write_analysis_base_to_file(filename, base):
    with open(filename, 'w', encoding='utf8') as file:
        for item in base:
            file.write(f'{item[0]} {item[1]}\n')


def read_file(filename):
    with open(filename, encoding='utf8') as file:
        result = file.read()
    return result


def is_english_char(char_value):
    char_index = ord(char_value)
    ord_big_letter_start = ord('A')
    ord_big_letter_end = ord('Z')
    ord_small_letter_start = ord('a')
    ord_small_letter_end = ord('z')
    if ord_small_letter_start <= char_index <= ord_small_letter_end:
        return True
    elif ord_big_letter_start <= char_index <= ord_big_letter_end:
        return True
    return False


def get_sorted_analysis_base(base):
    total_chars = sum(base.values())
    stats = [(k, round((v / total_chars), 3)) for k, v in base.items()]
    result = sorted(stats, key=(lambda item: (-item[1], item[0])))
    return result


def main():
    filename_for_read = 'text.txt'
    filename_for_write = 'analysis.txt'
    char_base = {}
    if is_file_exists(filename_for_read):
        data = read_file(filename_for_read)
        for char in data:
            if is_english_char(char):
                char_lower = char.lower()
                if char_lower in char_base:
                    char_base[char_lower] += 1
                else:
                    char_base[char_lower] = 1
        analysis_base = get_sorted_analysis_base(char_base)
        write_analysis_base_to_file(filename_for_write, analysis_base)
    else:
        print(f'Файла {filename_for_read} не существует!')


if __name__ == '__main__':
    main()
