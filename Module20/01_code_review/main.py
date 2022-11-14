students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_id_age_pairs(base):
    return [(key, value['age']) for key, value in base.items()]


def get_all_students_interests(base):
    return [interest for item in students.values()
            for interest in item['interests']]


def get_all_last_names_length(base):
    return sum([len(item['surname']) for item in base.values()])


def main():
    id_age_pairs = get_id_age_pairs(students)
    all_students_interests = get_all_students_interests(students)
    all_last_name_length = get_all_last_names_length(students)
    print(f'Список пар "ID студента — возраст": {id_age_pairs}')
    print(f'Полный список интересов всех студентов: {all_students_interests}')
    print(f'Общая длина всех фамилий студентов: {all_last_name_length}')


if __name__ == '__main__':
    main()
