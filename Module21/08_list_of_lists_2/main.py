nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def get_flat_array(array, result_array=[]):
    for item in array:
        if isinstance(item, list):
            get_flat_array(item)
        else:
            result_array.append(item)
    return result_array


def main():
    result = get_flat_array(nice_list)
    print(result)


if __name__ == '__main__':
    main()
