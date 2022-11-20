def read_and_reverse_file(filename='zen.txt'):
    result = ''
    with open(filename) as file:
        for line in file.readlines()[::-1]:
            result += line
    return result[:-1]


def main():
    reversed_data = read_and_reverse_file()
    print(reversed_data)


if __name__ == '__main__':
    main()
