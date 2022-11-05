def crypt(string, offset=3):
    result = ''
    for char in string:
        char_index = ord(char)
        ord_big_letter_start = ord('А')
        ord_big_letter_end = ord('Я')
        ord_small_letter_start = ord('а')
        ord_small_letter_end = ord('я')
        if ord_big_letter_start <= char_index <= ord_big_letter_end:
            if char_index + offset > ord_big_letter_end:
                result += chr(ord_big_letter_start + (
                    char_index + offset - ord_big_letter_end - 1))
            else:
                result += chr(char_index+3)
        elif ord_small_letter_start <= char_index <= ord_small_letter_end:
            if char_index + offset > ord_small_letter_end:
                result += chr(ord_small_letter_start + (
                    char_index + offset - ord_small_letter_end - 1))
            else:
                result += chr(char_index+3)
        else:
            result += char
    return result


if __name__ == '__main__':
    result = crypt('это питон ЭТО ПИТОН')
    print(result)
