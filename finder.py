""" Finder CLI - Script to run through the codebase and find instances of words.

Usage:
finder.py <dir>
finder.py <dir> (-s <save> | --save=<save>)
finder.py (-h | --help)

Options:
    -h --help                          Show the programs help page.
    -s<save> --save=<save>             Indicates the output should be saved.

Arguments:
    <dir>                              The string representing the directory.
    <save>                             The save directory to use.
"""

from colorama import Fore, Back, Style
from colorama import init as colour_init
from docopt import docopt
from typing import List, Dict, NoReturn
from arg_parsing import Argument, ParsedArgument, ArgumentOption
from file_tree import Node, FileNode, FolderNode, NodeError, view_node
import file_utils
import folder_utils


# TODO : Should really be a builder in the file_tree.py script
def build_file_tree(path: str) -> Node:
    return get_node(path)


def get_node(path: str) -> Node:

    if file_utils.is_file(path):
        return FileNode(path)
    elif folder_utils.is_folder(path):
        curr_node = FolderNode(path)

        abs_path = file_utils.get_abs_path(path)
        child_names = [folder_utils.join_path(abs_path, f) for f in folder_utils.get_files(path)]
        files = [f for f in child_names if file_utils.is_file(f)]
        folders = [f for f in child_names if folder_utils.is_folder(f)]

        for f in files:
            curr_node.add_child(FileNode(f))
        for f in folders:
            curr_node.add_child(get_node(f))

        return curr_node

    else:
        raise NodeError("Invalid Node type for path")


def parse_arg(argument: Argument, doc_args: Dict[str, str]) -> ParsedArgument:
    """
    This function will return the parsed argument
    from the docopt parsed argument dictionary.
    :param argument: The argument object representing an arg to
    be parsed.
    :param doc_args: Parsed docopt arguments
    :return: A ParsedArgument object representing the parsed arg.
    """
    value = False
    short = ""  # The short option (E.g. "-s")
    long = ""   # The long option (E.g. "--save")

    can_get_val = True
    if argument.option.is_valid():
        if argument.option.short:
            short = "-" + argument.option.short
        if argument.option.long:
            long = "--" + argument.option.long

        if not (doc_args[short] or doc_args[long]):
            can_get_val = False

    if argument.arg:
        if can_get_val:
            value = doc_args[argument.arg]
    else:
        value = True

    return ParsedArgument(argument.arg, argument.description, value, argument.option)


def main() -> NoReturn:
    to_parse = [
        Argument("<dir>", "root directory"),
        Argument("<save>", "save directory for output.", ArgumentOption("s", "save")),
    ]

    # Should be run on Windows, not necessary to have
    # on Linux but won't kill us
    colour_init()
    arguments = docopt(__doc__)
    print(arguments)

    print(Fore.CYAN + "\n======Running Main CLI======" + Style.RESET_ALL)
    print("Arguments Parsed:")
    # Simply mapping all the arguments by mapping the arguments
    # to be parsed with the parse_arg func
    parsed = [parse_arg(a, arguments) for a in to_parse]
    valid_parsed = [a for a in parsed if a.is_valid()]
    valid_parsed.sort(key=lambda x: x.arg)

    for arg in valid_parsed:
        print("Argument: %s" % arg.arg)
        print("Value: %s" % arg.value)
        print("Description: %s" % arg.description)
    print("================================")

    root_folder = [arg.value for arg in valid_parsed if arg.arg == "<dir>"][0]
    root = build_file_tree(root_folder)
    view_node(root)


if __name__ == "__main__":
    main()
