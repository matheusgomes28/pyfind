# file_tree.py - Contains the code for the file structure
import file_utils as fu
from __future__ import annotations
from typing import NoReturn


class NodeError(Exception):

    def __init__(self, message):
        self.message = message


class ChildNumberException(NodeError):

    def __init__(self, number):
        super().__init__("Node number given for child is out of bounds")
        self.number = number


class Node(object):

    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, child: Node) -> NoReturn:
        """
        Function that adds the given child to the
        list of children of this node.
        :param child: Node object representing the
        child.
        :return: void
        """
        self.children.append(child)

    def get_child(self, num: int) -> Node:
        """
        Gets the nTh child of this node. Throws error
        if the child number goes over the bounds.
        :param num: Integer representing position of child.
        :return: Node object representing the child.
        """

        if 0 <= num < len(self.children):
            return self.children[num]

        # If it reached this, num is out of bounds
        raise ChildNumberException(num)


# TODO Finish implementing this class
class FolderNode(Node):
    pass


# TODO finish implementing this class
class FileNode(Node):
    pass
