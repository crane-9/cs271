"""
Module contains a single class for the assembler's `SymbolicTable`, which serves to keep track of the input script's defined and pre-defined variables.
"""


class SymbolicTable:
    """
    Table that keeps a relationship between symbolic labels and values/addresses.
    """

    def __init__(self):
        """
        Initializes an empty table.
        """

    def add_entry(self, symbol: str, addr: int) -> None:
        """
        Adds the pair to the table.
        :param symbol: The "variable name" or symbolic name of the value.
        :param addr: The numerical address to link to the symbol.
        """

    def contains(self, symbol: str) -> bool:
        """
        Checks that the table contains the given symbol.
        :param symbol: The "variable name" to check for within the table.
        :returns: True if the given symbol exists in the table.
        """

    def get_address(self, symbol: str) -> int:
        """
        Gets the address (int) tied to the given symbol (string).
        :param symbol: The "variable name" to retrieve the value of.
        :returns: The address attached to the given symbolic name.
        """
