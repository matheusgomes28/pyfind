from typing import NoReturn
import file_utils as fu


class FileException(Exception):
    pass


class File(object):

    def __init__(self, file_path: str):
        self.file_path = fu.get_abs_path(file_path)

        try:
            self.file_handle = open(self.file_path, "r")
        except IOError as e:
            print("Error opening file: %s" % e)
            self.file_handle = None

    def read_line(self) -> str:
        """
        Reads the line number given, returning it as
        a string.
        :return: String with the contents of the line given.
        """

        if self.file_handle:
            try:
                return self.file_handle.readline()
            except IOError as e:
                raise FileException()
        else:
            # TODO : add meaningful messages
            # File is not open here
            raise FileException()

    def read_all(self):
        """
        Reads the whole file as a string.
        :return: String representing the contents of
        the file.
        """
        if self.file_handle:
            try:
                return self.file_handle.readlines()
            except IOError as e:
                raise FileException
        else:
            raise FileException

    def reset(self) -> NoReturn:
        """
        Takes reader pointer to the beginning of the file.
        :return: void
        """
        pass

    def close(self) -> NoReturn:
        """
        Closes the file handle.
        :return: void
        """
        if self.file_handle:
            self.file_handle.close()


def main() -> NoReturn:
    # Testing code
    file = File("finder.py")
    print(file.read_line(), end="")
    print(file.read_line(), end="")
    print(file.read_line(), end="")
    print(file.read_line(), end="")
    file.close()


if __name__ == "__main__":
    main()
