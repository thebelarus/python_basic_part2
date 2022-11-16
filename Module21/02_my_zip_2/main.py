def get_custom_zip(*args):
    min_length = min([len(arg) for arg in args])
    return [tuple(list(item)[iteration]
            for (item) in args)
            for iteration in range(min_length)
            ]


def main():
    value_1 = [1, 2, 3, 4, 5]
    value_2 = {1: "s", 2: "q", 3: 4}
    value_3 = (1, 2, 3, 4, 5)
    my_zip = get_custom_zip(
        value_1,
        value_2,
        value_3
    )
    print(my_zip)
    value_1 = [{"x": 4}, "b", "z", "d"]
    value_2 = (10, {20}, [30], "z")
    my_zip = get_custom_zip(
        value_1,
        value_2,
    )
    print(my_zip)


if __name__ == '__main__':
    main()
