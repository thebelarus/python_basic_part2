class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.is_calm = True

    def get_about_me(self):
        return (
            f'My name {self.name}, i\'m {self.age} years old, '
            f'is hungry: {self.is_hungry}, is calm: {self.is_calm}')

    def __str__(self):
        return self.get_about_me()


class Parent:
    def __init__(self, name, age, children=[]):
        self.name = name
        self.age = age
        self.children = []
        if self.is_valid_inital_children_array(children):
            self.children = children

    def is_valid_inital_children_array(self, children):
        return all([
            child for child in children
            if self.is_child_valid_for_me(child)]
            )

    def is_child_valid_for_me(self, child):
        return self.age - child.age > 16

    def get_about_me(self):
        children_info = '\n\t'.join(
            [child.get_about_me() for child in self.children])
        return (
            f'My name {self.name}, i\'m {self.age} years '
            f'old, my children: \n\t{children_info}')

    def add_child(self, child):
        if self.is_child_valid_for_me(child):
            self.children.append(child)

    def feed_child(self, child: Child):
        if child.is_hungry:
            child.is_hungry = False

    def calm_child(self, child: Child):
        if child.is_calm:
            child.is_calm = False


def main():
    child_1 = Child('Juzy', 10)
    child_2 = Child('Samantha', 8)
    child_3 = Child('Nicole', 6)
    parent = Parent('Rick', 30, [child_1, child_2, child_3])
    print(parent.get_about_me())
    parent.feed_child(child_1)
    parent.feed_child(child_2)
    print(parent.get_about_me())


if __name__ == '__main__':
    main()
