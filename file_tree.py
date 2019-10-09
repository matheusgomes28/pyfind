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
            raise ChildNumberException("Children index out of bounds")

    def __repr__(self):
        child_repr = repr(self.children)[0:40] + "...]"
        return "({:s}, Name: {:s}, Children: {:.43s})".format(self.__class__.__name__, self.name, child_repr)

    def __str__(self):
        return "({:s}, Name: {:s}, N Children: {:d})".format(self.__class__.__name__, self.name, len(self.children))


# TODO : Perhaps add some class docstrings here
class FolderNode(Node):

    def __init__(self, path: str):

        if not folder_utils.is_folder(path):
            raise FolderNodeError("Path given is not a valid folder")

        super().__init__(folder_utils.get_dir_name(path))
        self.path = path


# TODO : Perhaps add some class docstrings here
class FileNode(Node):

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
        all_props = set(dir(self.__class__)) | set(self.__dict__.keys())
        filtered = all_props - set(["add_child", "get_child"])
        return filtered
