#!usr/bin/env python
"""
Module contains a single class for the assembler's `SymbolicTable`, which serves to keep track of the input script's defined and pre-defined variables.
"""
from errors import *


class SymbolicTable:
    """
    Table that keeps a relationship between symbolic labels and values/addresses.
    """

    def __init__(self):
        """
        Initializes an empty table.
        """
        self.__table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576
        }
        # Procedurally add R0 - R15
        self.__table.update({f'R{idx}': idx for idx in range(0, 16)})

    def add_entry(self, symbol: str, addr: int) -> None:
        """
        Adds the pair to the table.
        :param symbol: The "variable name" or symbolic name of the value.
        :param addr: The numerical address to link to the symbol.
        """
        if self.contains(symbol):
            raise SymbolicTableError(f"Symbol '{symbol}' already exists.")
        
        self.__table[symbol] = addr

    def contains(self, symbol: str) -> bool:
        """
        Checks that the table contains the given symbol.
        :param symbol: The "variable name" to check for within the table.
        :returns: True if the given symbol exists in the table.
        """
        return symbol in self.__table.keys()

    def get_address(self, symbol: str) -> int:
        """
        Gets the address (int) tied to the given symbol (string).
        :param symbol: The "variable name" to retrieve the value of.
        :returns: The address attached to the given symbolic name.
        """
        if not self.contains(symbol): 
            raise SymbolicTableError(f"Symbol '{symbol}' does not exist.")
        
        return self.__table[symbol]
