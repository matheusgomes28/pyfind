# file_tree.py - Contains the code for the file structure
from __future__ import annotations
import folder_utils
import file_utils
from typing import NoReturn


class NodeError(Exception):
    pass


class ChildNumberException(NodeError):

    def __init__(self, number: int):
        super().__init__("Node number given for child is out of bounds")
        self.number = number


class FolderNodeError(NodeError):

    def __init__(self, message: str):
        super().__init__(message)


class FileNodeError(NodeError):

    def __init__(self, message: str):
        super().__init__(message)


class Node(object):
    """
    Parent of all the node objects. This represents a
    Node in a tree, it may have children.
    """

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
        return self[num]

    # So we can iterate through child nodes
    def __len__(self) -> int:
        return len(self.children)

    # So we can iterate through child nodes
    def __getitem__(self, item: int) -> Node:
        if 0 <= item < len(self):
            return self.children[item]
        else:
            raise IndexError

    def __repr__(self):
        child_repr = repr(self.children)[0:40] + "...]"
        return "({:s}, Name: {:s}, Children: {:.43s})".format(self.__class__.__name__, self.name, child_repr)

    def __str__(self):
        return "({:s}, Name: {:s}, N Children: {:d})".format(self.__class__.__name__, self.name, len(self.children))


class FolderNode(Node):
    """
    This is the representation of a folder in the file
    tree. Note that the children of this object may be
    another folder or a file.
    """

    def __init__(self, path: str):

        if not folder_utils.is_folder(path):
            raise FolderNodeError("Path given is not a valid folder")

        super().__init__(folder_utils.get_dir_name(path))
        self.path = path


class FileNode(Node):
    """
    This is the representation of a file in the file
    tree. Note that this object cannot have any children,
    so the get/add children objects are deleted.
    """

    def __init__(self, path: str):

        if not file_utils.is_file(path):
            raise FileNodeError("Path given is not a valid file")

        super().__init__(file_utils.get_filename(path))
        self.path = path

    # Elegantly removing the add/get for children
    def __getattribute__(self, name):
        if name in ["add_child", "get_child"]:
            raise AttributeError("Deleted attribute: " + name)
        else:
            return super(FileNode, self).__getattribute__(name)

    # Elegantly removing the add/get for children
    def __dir__(self):
        all_props = {dir(self.__class__)} | {self.__dict__.keys()}
        filtered = all_props - {"add_child", "get_child"}
        return filtered


def view_node(node: Node, n: int = 0) -> NoReturn:
    print_f = print  # May be a file output or something
    trail = "|" + "-" * (n*2)
    print_f(trail + "{:s}".format(node.name))

    if node.__class__ == FolderNode:
        for child in node:
            view_node(child, n + 1)
