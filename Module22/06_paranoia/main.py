import os


def crypt(string, offset=3):
    result = ''
    for char in string:
        char_index = ord(char)
        ord_big_letter_start = ord('A')
        ord_big_letter_end = ord('Z')
        ord_small_letter_start = ord('a')
        ord_small_letter_end = ord('z')
        if ord_big_letter_start <= char_index <= ord_big_letter_end:
            if char_index + offset > ord_big_letter_end:
                result += chr(ord_big_letter_start + (
                    char_index + offset - ord_big_letter_end - 1))
            else:
                result += chr(char_index + offset)
        elif ord_small_letter_start <= char_index <= ord_small_letter_end:
            if char_index + offset > ord_small_letter_end:
                result += chr(ord_small_letter_start + (
                    char_index + offset - ord_small_letter_end - 1))
            else:
                result += chr(char_index + offset)
        else:
            result += char
    return result


def is_file_exists(filename_value):
    filepath = os.path.join(os.getcwd(), filename_value)
    if os.path.exists(filepath):
        return True
    return False


def main():
    filename_for_read = 'text.txt'
    filename_for_write = 'cipher_text.txt'
    data = ''
    offset = 1
    if is_file_exists(filename_for_read):
        with open(filename_for_read, encoding='utf') as file:
            for line in file.readlines():
                data += crypt(line, offset=offset)
                offset += 1
        with open(filename_for_write, 'w', encoding='utf') as file:
            file.write(data)
    else:
        print(f'Файла {filename_for_read} не существует!')


if __name__ == '__main__':
    main()
