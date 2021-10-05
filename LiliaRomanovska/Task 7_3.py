import time
from contextlib import contextmanager, ContextDecorator
from time import perf_counter

""" 
    Implement decorator with context manager support for writing execution time to log-file. 
"""

class context_manager_execution_time(ContextDecorator):

    def __init__(self, filename, mode='a'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Exception: {exc_type} - {exc_value}\n")
        else:
            with open(filename, "a") as file:
                file.write(f"Execution time {(perf_counter() - start_time):.4f} sec\n")

@context_manager_execution_time
def func_execution_time(first_arg: int, second_arg: int):
    return (first_arg*second_arg)**2


