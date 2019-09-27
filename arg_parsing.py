class ArgumentException(Exception):
    pass


class ArgumentOption(object):

    def __init__(self, short: chr, long: str = ""):
        self.short = short
        self.long = long

    def __repr__(self):
        return "({:s}, {:s})".format(self.short, self.long)

    def __str__(self):
        return "Option ({:s}, {:s})".format(self.short, self.long)

    def is_valid(self) -> bool:
        return self.long or self.short


class Argument(object):
    """
    This class represents a command line argument
    which may or may not be already parsed.
    """

    def __init__(self, argument: str, desc: str, option: ArgumentOption = ArgumentOption("", "")):
        self.arg = argument
        self.description = desc
        self.option = option


class ParsedArgument(Argument):
    """
    This class represents an argument that
    has already been parsed.
    """

    def __init__(self, argument: str, desc: str, value: str, option: ArgumentOption = ArgumentOption("", "")):
        super(ParsedArgument, self).__init__(argument, desc, option)
        self.value = value
        self.success = False

    def is_valid(self) -> bool:
        return not not self.value

    def __repr__(self):
        return "ParsedArgument(%s, %s, %s)" % (self.arg, self.value, self.description)

    def __str__(self):
        return "(name: {:s}, value: {:s})".format(self.arg, self.value)
