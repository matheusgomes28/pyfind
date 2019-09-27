from typing import List, NoReturn
import os


def get_files(path: str) -> List[str]:
    """
    This function will get the files under
    the folder path given.
    :param path: String representing the directory path.
    :return: List of files under the given directory.
    """
    if not path:
        return os.listdir()

    return os.listdir(path)


def filter_files(path_list: List[str]) -> List[str]:
    """
    This function will filter the list given so
    only the file names will be kept.
    :param path_list: List of strings which may be files, folders etc.
    :return: List of strings representing only files.
    """
    return [i for i in path_list if os.path.isfile(i)]


def filter_folders(path_list: List[str]) -> List[str]:
    """
    This function will filter the list given
    so only the directory names will be kept
    :param path_list: List of string representing files, dirs, etc.
    :return: List of string representing only the directories.
    """
    return [i for i in path_list if os.path.isdir(i)]


def main() -> NoReturn:
    print("==Running the test code==")
    print("Current working dir is: %s" % os.getcwd())
    print("The files under this directory are: %s" % get_files(""))

    # Get the files and directories under this folder
    path = "."
    dir_contents = os.listdir(path)

    print("The files contained in this dir are: %s" % filter_files(dir_contents))
    print("The directories contained in this dir are: %s" % filter_folders(dir_contents))


if __name__ == "__main__":
    main()
