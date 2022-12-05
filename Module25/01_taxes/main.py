class Property:
    def __init__(self, worth) -> None:
        self.worth = worth

    def count_property(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def count_property(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def count_property(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def count_property(self):
        return self.worth / 500


def main():
    apartment = Apartment()
    apartment = Car()
    apartment = CountryHouse()


if __name__ == '__main__':
    main()
