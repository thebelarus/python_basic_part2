def array_sort(array) -> None:
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    array_input = [1, 4, -3, 0, 10]
    print(f'Изначальный список: {array_input}')
    array_sort(array_input)
    print(f'Отсортированный список: {array_input}')
