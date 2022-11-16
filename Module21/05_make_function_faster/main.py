def calculating_math_func(data, cache={}):
    if data in cache:
        return cache[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    cache[data] = result
    return result


def main():
    result = calculating_math_func(10)
    print(result)
    result = calculating_math_func(15)
    print(result)
    result = calculating_math_func(10)
    print(result)


if __name__ == '__main__':
    main()
