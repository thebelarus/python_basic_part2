def read_and_reverse_file(filename='zen.txt'):
    chars_base = {}
    char_amount = 0
    words_amount = 0
    lines_amount = 0
    with open(filename) as file:
        for line in file.readlines():
            lines_amount += 1
            for word in line.split():
                words_amount += 1
                for char in word:
                    char_amount += 1
                    add_char_to_base(chars_base, char)
    rare_char = get_rare_char_from_base(chars_base)
    return (char_amount,
            words_amount,
            lines_amount,
            rare_char
            )


def add_char_to_base(base, char):
    char_to_lower = char.lower()
    if char_to_lower.isalpha():
        if char_to_lower in base:
            base[char_to_lower] += 1
        else:
            base[char_to_lower] = 1


def get_rare_char_from_base(base):
    return [
        key for key, value in base.items()
        if value == min(base.values())
    ][0]


def main():
    (
        char_amount_value,
        words_amount_value,
        lines_amount_value,
        rare_char_value
    ) = read_and_reverse_file()
    print(f'Количество букв в файле: {char_amount_value}')
    print(f'Количество слов в файле: {words_amount_value}')
    print(f'Количество строк в файле: {lines_amount_value}')
    print(f'Наиболее редкая буква: {rare_char_value}')


if __name__ == '__main__':
    main()
