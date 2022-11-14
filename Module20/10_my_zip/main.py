

def get_custom_zip(array_1, array_2):
    min_length = min(len(array_1), len(array_2))
    return ((array_1[item], array_2[item]) for item in range(min_length))


def main():
    my_zip = get_custom_zip('abcd', (10, 20, 30, 40, 50))
    print(my_zip)
    for item in my_zip:
        print(item)


if __name__ == '__main__':
    main()
