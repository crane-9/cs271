#!usr/bin/env python
"""
Holds various error to be thrown throughout the assembler.
"""

class AssemblerError(Exception):
    """ An error raised in the process of assembly. Parent of all following exceptions. """


class CodeError(AssemblerError):
    """ An error raised in the process of translating mnemonics to bits. """


class ParseError(AssemblerError):
    """ An error raised in the process of parsing. """


class SymbolicTableError(AssemblerError):
    """ An error raised in the symbolic table. """

