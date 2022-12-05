class Stack:
    def __init__(self):
        self.__data = []

    def put(self, value):
        self.__data.insert(0, value)

    def pop(self):
        return self.__data.pop(0)

    def __len__(self):
        return len(self.__data)


class TaskManager:
    def __init__(self):
        self.__stack = Stack()

    def new_task(self, task_txt, task_priority):
        self.__stack.put((task_txt, task_priority))

    def __str__(self):
        temp = {}
        while len(self.__stack) != 0:
            text, priority = self.__stack.pop()
            if priority in temp:
                temp[priority].append(text)
            else:
                temp[priority] = [text]
        result = [
            f"{key} {'; '.join(temp[key])}"
            for key in sorted(temp.keys())
            ]
        return 'Результат:\n' + '\n'.join(result)


def main():
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    print(manager)


if __name__ == '__main__':
    main()
