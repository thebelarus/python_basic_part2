import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def generate_site(name, template):
    result = copy.deepcopy(template)
    result['html']['body']['h2'] = result['html']['body']['h2'].replace(
        'iphone', name)
    return result


def main():
    sites_storage = {}
    sites_count = int(input('Сколько сайтов: '))
    for _ in range(sites_count):
        product_name = input('Введите название продукта для нового сайта: ')
        sites_storage[product_name] = generate_site(
            product_name,
            site
        )
        for site_name, site_data in sites_storage.items():
            print(f'Сайт для {site_name}: ')
            print(f'site = {site_data}')


if __name__ == '__main__':
    main()
