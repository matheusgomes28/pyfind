from typing import NoReturn
import file_utils as fu


class FileException(Exception):
    pass


class File(object):

    def __init__(self, file_path: str):
        self.file_path = fu.get_abs_path(file_path)

    def read_line(self) -> str:
        """
        Reads the line number given, returning it as
        a string.
        :return: String with the contents of the line given.
        """

        with open(self.file_path, "rt") as f:
            return f.readline()

    def reset(self) -> NoReturn:
        """
        Takes reader pointer to the beginning of the file.
        :return: void
        """
        pass


def main() -> NoReturn:
    file = File("finder.py")
    print(file.read_line())


if __name__ == "__main__":
    main()
