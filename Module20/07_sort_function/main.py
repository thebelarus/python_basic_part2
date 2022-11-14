def tpl_sort(*params):
    is_correct_params = all([isinstance(param, int) for param in params])
    if not is_correct_params:
        return params
    array = list(params)
    array_length = len(array) - 1
    for item_out in range(array_length):
        for item_in in range(array_length - item_out):
            if array[item_in] > array[item_in + 1]:
                array[item_in], array[item_in +
                                      1] = array[item_in + 1], array[item_in]
    return tuple(array)


def main():
    print(tpl_sort(6, 3, -1, 8, 4, 10, -5))


if __name__ == '__main__':
    main()
