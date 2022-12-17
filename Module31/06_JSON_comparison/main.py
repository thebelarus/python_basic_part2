import json
from typing import Dict, Any, List, Generator


def get_json_data_from_file(filename: str) -> Dict[str, str]:
    '''Функция чтения JSON файла и преобразования в словарь.'''
    with open(filename, encoding='utf8') as file:
        data = json.load(file)
        return data


def search_item_in_dataset(
        dict_var: Dict[str, Any],
        key_search: str) -> Generator[Any, None, None]:
    '''Генератор поиска ключа в словаре из массива параметров.'''
    for key, value in dict_var.items():
        if key == key_search:
            yield value
        elif isinstance(value, dict):
            for key_new in search_item_in_dataset(value, key_search):
                yield key_new


def search_items_in_dataset(
        data: Dict[str, Any],
        search_items_dataset: List[str]) -> Dict[str, Any]:
    '''Функция поиска ключей в словаре данных.'''
    result: Dict[str, Any] = {}
    for item_for_search in search_items_dataset:
        result[item_for_search] = list(
            search_item_in_dataset(data, item_for_search))
    return result


def find_datasets_diff(
        dataset_1: Dict[str, Any],
        dataset_2: Dict[str, Any],
        storage: Dict[str, Any] = {}) -> Dict[str, Any]:
    '''Функция поиска отличий в двух словаря данных данных.'''
    for key, _ in zip(dataset_1, dataset_2):
        if type(dataset_1[key]) is dict:
            storage[key] = {}
            find_datasets_diff(dataset_1[key], dataset_2[key], storage[key])
        if dataset_1[key] != dataset_2[key]:
            storage[key] = dataset_1[key]
    return storage


def write_dataset_to_file(dataset: Dict[str, Any], filename: str) -> bool:
    '''Функция записи словаря данных в JSON файл.'''
    try:
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(dataset, file, indent=4)
    except Exception as error:
        print(error)
        return False
    else:
        return True


def main() -> None:
    '''Tестирование приложения'''
    json_old_dataset_filemame = 'json_old.json'
    json_new_dataset_filemame = 'json_new.json'
    json_result_dataset_filemame = 'result.json'
    diff_list = ['services', 'staff', 'datetime']
    old_json_data = get_json_data_from_file(json_old_dataset_filemame)
    new_json_data = get_json_data_from_file(json_new_dataset_filemame)
    old_data_parsed = search_items_in_dataset(old_json_data, diff_list)
    new_data_parsed = search_items_in_dataset(new_json_data, diff_list)
    result = find_datasets_diff(new_data_parsed, old_data_parsed)
    if write_dataset_to_file(result, json_result_dataset_filemame):
        print(f'Данные записаны в файл {json_result_dataset_filemame}')
    print(result)


if __name__ == '__main__':
    main()
