import os
from collections.abc import Iterable
from typing import Union


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.start = None
        self.size = 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        self.size += 1
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __str__(self) -> str:
        current = self.head
        result: list[str] = []
        while current:
            result.append(str(current.value))
            current = current.next
        return ' '.join(result)

    def get(self, index: int) -> Union[int, None]:
        if index >= self.size or index < 0:
            return None
        current = self.head
        node_index = 0
        while node_index <= index:
            if node_index == index:
                return current.value
            node_index += 1
            current = current.next

    def remove(self, index: int) -> None:
        if self.head is None:
            return
        current = self.head
        if index == 0:
            self.head = current.next
            current = None
            return
        for i in range(index - 1):
            current = current.next
            if current is None:
                break
        if current is None:
            return
        if current.next is None:
            return
        next_node = current.next.next
        current.next = next_node


def main() -> None:
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    print('Текущий список:', my_list)
    print('Получение третьего элемента:', my_list.get(2))
    print('Удаление второго элемента.')
    my_list.remove(1)
    print('Новый список:', my_list)


if __name__ == '__main__':
    main()
