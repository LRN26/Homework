class context_manager:

    """Context manager for opening and working with files,
    including handling exceptions."""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            print("File not found")
        else:
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type or exc_val or exc_tb:
            print(f"{exc_type}: {exc_val}\n")


with context_manager('Text.txt', 'r') as file_to_read:
    print(file_to_read.read())