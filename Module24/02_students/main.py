class Student:
    def __init__(self, name: str, group_number: int, progress: list[int]):
        self.name: str = name
        self.group_number: int = group_number
        self.progress: list[int] = progress

    def get_average_progress(self):
        return sum(self.progress) / len(self.progress)

    def __str__(self):
        return (
            f'name {self.name} group {self.group_number} '
            f'average {self.get_average_progress()}')


def main():
    student1: Student = Student('Jonh', 1, [1, 2, 3, 1, 4])
    student2: Student = Student('Bob', 1, [1, 2, 3, 1, 4])
    student3: Student = Student('Mick', 1, [3, 2, 4, 1, 5])
    students: list[Student] = [student1, student2, student3]
    sorted_students = sorted(
        students,
        key=lambda student: student.get_average_progress()
        )
    for student in sorted_students:
        print(student)


if __name__ == '__main__':
    main()
