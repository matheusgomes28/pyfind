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
        finally:
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
            finally:
                self.file_handle.close()

        # TODO : add meaningful messages
        # File is not open here
        raise FileException()

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
