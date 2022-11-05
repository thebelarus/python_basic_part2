def array_compress(array):
    for index in range(len(array)-1, -1, -1):
        if array[index] == 0:
            array.append(array.pop(index))
    return [item for item in array if item]


if __name__ == '__main__':
    array_size = int(input('Кол-во чисел в списке: '))
    array_input = []
    for index in range(array_size):
        while True:
            array_element_input = int(input(f'Введите елемент {index +1}: '))
            if 0 <= array_element_input <= 2:
                array_input.append(array_element_input)
                break
            else:
                print('Елемент, число от 0 до 2')
    result = array_compress(array_input)
    print(f'Список до сжатия: {array_input}')
    print(f'Список после сжатия: {result}')
