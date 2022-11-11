
def search_county_by_city(navigator: dict, city: str):
    result = [
        country for country, citys
        in navigator_base.items() if city in citys
    ]
    if not result:
        return False
    return result.pop()


if __name__ == '__main__':
    navigator_base = {}
    search_attemps = 3
    country_count_input = int(input('Количество стран: '))
    for country_number in range(1, country_count_input + 1):
        while True:
            country_citys_input = input(f'{country_number} страна: ')
            country_citys = country_citys_input.split()
            if len(country_citys) > 2:
                country = country_citys.pop(0)
                citys = country_citys
                navigator_base[country] = citys
                break
            print('Недостаточно данных для заполнения базы!')
    for search_attemp in range(1, search_attemps + 1):
        city_for_search = input(f'{search_attemp} город: ')
        result = search_county_by_city(navigator_base, city_for_search)
        if result:
            print(f'Город {city_for_search} расположен в стране {result}.')
        else:
            print(f'По городу {city_for_search} данных нет.')
