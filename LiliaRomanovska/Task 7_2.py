from contextlib import contextmanager

""" context manager for opening and working with file, 
    including handling exceptions with @contextmanager decorator.
"""


@contextmanager
def context_open_file(filename, mode='r'):
    try:
        file = open(filename, mode)
        yield file
    except Exception as err:
        print("Error")
    finally:
        file.close()


with context_open_file("Text.txt", "r") as file:
    print(file.read())
