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
from typing import List, Dict
from arg_parsing import Argument, ParsedArgument, ArgumentOption
import file_utils
import folder_utils


def parse_arg(argument: Argument, doc_args: Dict[str, str]):
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


def main():
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
        print()


if __name__ == "__main__":
    main()
