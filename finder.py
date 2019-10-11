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
from typing import List, Dict, NoReturn, NamedTuple
from arg_parsing import Argument, ParsedArgument, ArgumentOption
from file_tree import Node, FileNode, FolderNode, NodeError
import file_utils
import folder_utils
import io_utils
import json
import itertools


def get_all_file_nodes(root: FolderNode) -> List[FileNode]:

    def get_all_file_nodes_r(curr_node: Node):
        if curr_node.__class__ == FileNode:
            return [curr_node.path]
        elif curr_node.__class__ == FolderNode:
            children = [get_all_file_nodes_r(c) for c in curr_node]
            return list(itertools.chain(*children))
        else:
            raise NodeError("Not a valid node type to parse")

    return get_all_file_nodes_r(root)


def analyse_files(files: List[str], matches: List[str], extensions: List[str], ignore: bool, max_size: int) -> Dict[str, List[NamedTuple]]:
    occurrences = {}
    i = 0
    for file in files:
        print("Analysing {:.2f}   \r".format(100*i/len(files)), end="")

        if ignore:
            if not not extensions and file_utils.get_extension(file) in extensions:
                continue
        else:
            # Filter out non source files
            if not not extensions and file_utils.get_extension(file) not in extensions:
                continue

        # Filter out files that are too big
        if file_utils.get_file_size(file) > max_size:
            continue

        i += 1
        results = io_utils.find_in_file(file, matches)
        if len(results) > 0:
            occurrences[file] = results

    return occurrences, i


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
    print("Generating file tree...")
    root_node = Node.from_path(root_folder, FolderNode)

    print("Finding files...")
    all_files = get_all_file_nodes(root_node)
    print("Number of files found: {:d}".format(len(all_files)))

    print("Checking for word occurrences")

    finder_params = {
        "files": all_files,
        "matches": [" LFM ", " Server ", " server ", " NetView ", " Netview ", " netview "],
        "extensions": ["png", "jpg", "jpeg"],
        "ignore": True,
        "max_size": 3000000
    }
    occurrences, n = analyse_files(**finder_params)
    print("")
    print("Number of files analysed: {:d}".format(n))
    print("Number of files which contain the matches: {:d}".format(len(occurrences)))
    print("Preparing JSON data...")
    json_dump = {}
    for key in occurrences:
        json_dump[key] = [i._asdict() for i in occurrences[key]]

    print("Saving file to output.txt")

    with open("output.json", "w") as f:
        json.dump(json_dump, f)


if __name__ == "__main__":
    main()
