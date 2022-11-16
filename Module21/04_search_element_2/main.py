site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(param, base, dive=0, limit=0):
    if param in base:
        return base[param]
    if not base:
        return None
    dive += 1
    if dive == limit:
        return None
    for value in base.values():
        return search(param, value, dive, limit)


def main():
    result = search('head', site, limit=1)
    print(result)


if __name__ == '__main__':
    main()
