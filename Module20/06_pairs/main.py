import random


def gerete_array(count=10):
    return [random.randint(1, 100) for _ in range(10)]


def main():
    array = gerete_array()
    result = [(elem_1, elem_2)
              for elem_1, elem_2 in zip(array[::2], array[1::2])]
    print(result)


if __name__ == '__main__':
    main()
