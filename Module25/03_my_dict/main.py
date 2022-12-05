class MyDict(dict):
    def get(self, key):
        return super().get(key, 0)


def main():
    my_dict = MyDict({'a': 111, 'b': 22})
    print(my_dict.get('a'))
    print(my_dict.get('c'))


if __name__ == '__main__':
    main()
