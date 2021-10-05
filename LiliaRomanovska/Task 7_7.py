class MyNumberCollection:

    def __init__(self, start, end=None, step=None):
        self.start = start
        self.end = end
        self.step = step
        self.collection = []
        if isinstance(start, tuple):
            for number in start:
                if isinstance(number, int):
                    self.collection.append(number)
                else:
                    raise TypeError(f"MyNumberCollection supports only numbers!")
        if isinstance(start, int):
            for number in range(self.start, self.end, self.step):
                self.collection.append(number)
            self.collection.append(end)

    def __repr__(self):
        return str(self.collection)

    def append(self, add_number):
        """appending new element to the end of collection"""
        if isinstance(add_number, int):
            self.collection.append(add_number)
        else:
            raise TypeError(" 'string' - object is not a number!")

    def __add__(self, other):
        """concatenating collections together using"""
        if isinstance(other, MyNumberCollection):
            return self.collection + other.collection
        else:
            raise TypeError("other variable have not a type(MyNumberCollection)")

    def __radd__(self, other):
        """concatenating collections together using"""
        return other.collection + self.collection

    def __getitem__(self, index):
        """when element is addressed by index(using []), user should get square of the addressed element."""
        return self.collection[index] ** 2

    def __iter__(self):
        return self

    def __next__(self):
        """when iterated using cycle for, elements should be given normally"""
        self.start += 1
        if self.start < len(self.collection):
            return self.collection[self.start]
        else:
            raise StopIteration


def main():
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    # [0, 2, 4, 5]
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    # [1, 2, 3, 4, 5]
    # col3 = MyNumberCollection((1, 2, 3, "4", 5))
    # TypeError: MyNumberCollection
    # supports only numbers!
    col1.append(7)
    print(col1)
    # [0, 2, 4, 5, 7]
    # col2.append("string")
    # TypeError: 'string' - object is not a number!
    print(col1 + col2)
    # [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
    print(col1)
    # [0, 2, 4, 5, 7]
    print(col2)
    # [1, 2, 3, 4, 5]
    print(col2[4])
    # 25
    for item in col1:
        print(item, end=" ")
    # 0 2 4 5 7


if __name__ == "__main__":
    main()
