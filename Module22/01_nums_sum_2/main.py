def parse_file(filename='numbers.txt'):
    amount = 0
    with open(filename) as file:
        for line in file.readlines():
            cleaned_line = line.strip()
            if cleaned_line:
                amount += int(cleaned_line)
    write_to_file(amount)


def write_to_file(data, filename='answer.txt'):
    with open(filename, 'w') as file:
        file.write(str(data))


def main():
    parse_file()


if __name__ == '__main__':
    main()
