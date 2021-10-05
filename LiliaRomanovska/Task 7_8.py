class MySquareIterator:

    """
        Implement your custom iterator class called MySquareIterator
        which gives squares of elements of collection it iterates through.
    """

    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.ind = 0
        return self

    def __next__(self):
        try:
            result = self.lst[self.ind] ** 2
            self.ind += 1
            return result
        except IndexError:
            raise StopIteration


def main():
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item, end=" ")


if __name__ == "__main__":
    main()
