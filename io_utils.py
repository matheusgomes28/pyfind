from typing import NoReturn, Type
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
                raise FileException("Error while reading the file.")
        else:
            raise FileException("File handle is not initialised")

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

    # So it can be used with if
    def __enter__(self):
        return self

    # TODO : find the proper type of this traceback
    def __exit__(self, except_type: Type, except_val: Exception, traceback: Type):

        # TODO : Find the proper way to handle exceptions in
        # this exit function
        if except_type == type(FileException):
            print("File Exception occurred")

        print("Closing file")
        self.file_handle.close()


def main() -> NoReturn:
    # Testing code
    file = File("finder.py")
    print(file.read_line(), end="")
    print(file.read_line(), end="")
    print(file.read_line(), end="")
    print(file.read_line(), end="")
    file.close()

    # Testing it reads the whole file
    with File("finder.py") as f:
        print(f.read_all())


if __name__ == "__main__":
    main()
