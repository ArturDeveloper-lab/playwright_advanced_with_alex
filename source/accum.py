class Accumulator:
    def __init__(self):
        self.__count = 0
        self.__brand = "Accumulator"

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def add_counts(self, count_to_add=1):
        self.__count += count_to_add
