def slicer(data, element):
    finded_elems = [
        index for index, value
        in enumerate(data) if value == element
    ]
    if not finded_elems:
        return tuple()
    elif len(finded_elems) == 1:
        return data[finded_elems[0]:]
    return data[finded_elems[0]:finded_elems[1]+1]


def main():
    print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
    print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2))


if __name__ == '__main__':
    main()
