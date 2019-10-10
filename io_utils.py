from types import TracebackType
from typing import NoReturn, Type, List, Tuple
import file_utils as fu
import sys

def LOG(error: str) -> NoReturn:
    print(error)

class FileException(Exception):
    pass


class File(object):

    def __init__(self, file_path: str):
        self.file_path = fu.get_abs_path(file_path)

        try:
            self.file_handle = open(self.file_path, "r", errors="ignore")
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
                raise FileException("Could not read lines. Maybe file is not open.")
        else:
            raise FileException("File handle does not exist.")

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

    def __exit__(self, except_type: Type, except_val: Exception, traceback: TracebackType):
        self.file_handle.close()

        def print_f(*args):
            pass

        if except_type:
            if except_type == FileException:
                print_f("Exception occurred: %s"% except_val)
                print_f("Closing file %s..." % self.file_path)
                return True
            else:
                LOG("Unknown error occurred in file: {:s}".format(self.file_path))
                sys.exit()


# TODO : Perhaps change the match obj to a list
def find_in_file(path: str, matches: List[str]) -> List[Tuple[int, str]]:
    lines = None  # Will hold the contents of each line
    with File(path) as f:
        # Should be [(line_n, contents)]
        lines = enumerate(list(f.file_handle))

    # Run the string checking in each of the lines
    return [(n + 1, s) for n, s in lines for match in matches if match in s]


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
        lines = list(f.file_handle)
        print("Number of lines is {:d}".format(len(lines)))

    print(find_in_file("io_utils.py", ["pass"]))


if __name__ == "__main__":
    main()
