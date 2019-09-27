from typing import NoReturn
import os


def get_extension(filename: str) -> str:
    """
    This function will get the file extension
    based on the file name.
    :param filename: The string representing the filename.
    :return: string representing the file extension, E.g. "txt".
    """
    return os.path.basename(filename).split('.')[-1]


def get_abs_path(filename: str) -> str:
    """
    This function will get the absolute path
    of the file path given
    :param filename: The file path. If it's already absolute then
    nothing should happen.
    :return: String representing the absolute path.
    """
    return os.path.abspath(filename)


def get_file_size(filename: str) -> int:
    """
    Get the file size of the given file.
    :param filename: String representing the file path.
    :return: Integer representing the size of the file.
    """

    if not os.path.exists(filename):
        raise Exception("File is not valid")

    return os.path.getsize(filename)


def file_exists(filename: str) -> bool:
    """
    Checks whether or not the file exists.
    :param filename: The string representing the filename.
    :return: Boolean representing whether or not file exists.
    """
    return os.path.exists(get_abs_path(filename))


def main() -> NoReturn:
    testing_path1 = "hello.txt"
    print("File extension of %s: %s" % (testing_path1, get_extension(testing_path1)))

    testing_path2 = "C:\\Users\\matheus.gomes\\hello.txt";
    print("File extension of %s: %s" % (testing_path2, get_extension(testing_path2)))

    testing_path3 = "C:/Users/matheus.gomes/hello.txt";
    print("File extension of %s: %s" % (testing_path3, get_extension(testing_path3)))

    print("Size of %s in bytes is: %d" % (testing_path2, get_file_size(testing_path2)))


if __name__ == "__main__":
    main()
