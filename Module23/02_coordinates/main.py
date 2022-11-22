import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("Деление на нуль в первой функции")


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return y / x
    except ZeroDivisionError:
        raise ZeroDivisionError("Деление на нуль во второй функции")


def main():
    data = []
    try:
        file = open('coord1inates.txt', 'r')
        for line in file:
            try:
                nums_list = line.split()
                file_2 = open('result.txt', 'a')
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join([str(item) for item in my_list])+'\n')
            except ZeroDivisionError as error:
                print(error)
            except Exception as error:
                print(f'Что-то пошло не так : {error}')
            finally:
                file_2.close()
    except FileNotFoundError:
        print(f'Файл не найден!')
    else:
        file.close()


if __name__ == '__main__':
    main()
