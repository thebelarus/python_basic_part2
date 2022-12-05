class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def get_presonal_info(self):
        return f'{self.__first_name} {self.__last_name}, {self.__age} лет'


class Employee(Person):
    def count_salary(self):
        pass


class Manager(Employee):
    def count_salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, first_name, last_name, age, sales):
        super().__init__(first_name, last_name, age)
        self.sales = sales

    def count_salary(self):
        return 5000 + 0.05 * self.sales


class Worker(Employee):
    def __init__(self, first_name, last_name, age, worked_hours):
        super().__init__(first_name, last_name, age)
        self.worked_hours = worked_hours

    def count_salary(self):
        return 100 + self.worked_hours


def main():
    workers = [
        Worker('Вася', 'Петров', 20, 100),
        Worker('Петя', 'Иванов', 30, 110),
        Worker('Коля', 'Сидоров', 30, 110),
        Manager('Костя', 'Петров', 20),
        Manager('Толя', 'Сидоров', 30),
        Manager('Валера', 'Иванов', 30),
        Agent('Аня', 'Петрова', 22, 700),
        Agent('Катя', 'Иванова', 33, 800),
        Agent('Юля', 'Сидорова', 26, 900),
    ]
    for worker in workers:
        salary = worker.count_salary()
        personal_info = worker.get_presonal_info()
        print(f'{personal_info}, зарплата: {salary}')


if __name__ == '__main__':
    main()
