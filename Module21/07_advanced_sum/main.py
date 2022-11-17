def sum(*args):
    amount = 0
    for arg in args:
        if isinstance(arg, list):
            amount += sum(*arg)
        else:
            amount += arg
    return amount


def main():
    result = sum([[1, 2, [3]], [1], 3])
    print(result)
    result = sum(1, [2], 3, 4, 5)
    print(result)


if __name__ == '__main__':
    main()
