import json
from file_tree import Node, FolderNode
from typing import NoReturn, Callable


def _console_view_helper(node: Node, print_f: Callable[[str], NoReturn], n: int) -> NoReturn:
    trail = "|" + "-"*n
    print_f(trail + "{:s}".format(node.name))

    if node.__class__ == FolderNode:
        for child in node:
            _console_view_helper(child, print_f, n + 1)


def console_view(root_node: Node, print_f: Callable[[str], NoReturn] = print) -> NoReturn:
    """
    This class returns a string which can be printed
    in a console.
    :param root_node: The root node from where to start with.
    :param print_f: Function to use for printing the value out.
    :return: void
    """
    _console_view_helper(root_node, print_f, 0)


# TODO : Implement this, should save to file
def json_view(root_node: Node) -> NoReturn:
    pass
