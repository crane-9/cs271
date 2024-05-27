#!usr/bin/env python
from enum import Enum

from errors import *


class CommandType(Enum):
    """
    Three command types.
    """
    A_COMMAND  # Command changes the A-reg value (@Xxx)
    C_COMMAND  # Command follows the scheme dest=comp;jump
    L_COMMAND  # Pseudo-command.


class Parser:
    """
    Controls access to the input code. Reads and parses line-by-line, removing whitespace and comments as needed.
    """

    def __init__(self, input_file: str):
        """
        Initialize the parser for a specific file.
        This cosntructor opens the file and prepares parsing.
        :param input_file: Path to the given input file.
        """
        self.current_line = 0
        self.current_command = ""  # Empty initial command.
        
        # Retrieve all lines.
        with open(input_file, 'r') as fp:
            self.lines = fp.readlines()

    def hasMoreCommands(self) -> bool:
        """
        Checks if there are more commands in the input file to parse.
        Skips comments and empty lines.
        :return: True if there are more lines to parse.
        """

        def is_command_line(line: str) -> bool:
            """ Checks that the givne line is valid (not empty or a comment). """
            # Clean
            line = line.strip()
            # Check if comment.
            if line.startswith("//"):  return False
            # Return not empty status.
            return line is not ""
            
        
        # Cycle through lines until a valid line is found.
        while len(self.lines) > 0:
            # Check: ignore comments and whitespace
            if not is_command_line(self.lines[0]):
                self.current_line += 1
                line = self.lines.pop(0)  # Remove and ignore line.
                continue

            # Else,
            return True
        else:
            # If loop ends, no lines remain.
            return False

        

    def advance(self) -> None: 
        """
        Called only if `hasMoreCommands` is true.
        Reads from input and sets the new `current_command`.
        """
        self.current_line += 1
        self.current_command = self.lines.pop(0).strip()

    def command_type(self) -> CommandType:
        """
        Parse the `CommandType` of `current_command`.
        :returns: A `CommandType` enum describing the current command.
        """
        if self.current_command.startswith("(") and self.current_command.endswith(")"):
            return CommandType.L_COMMAND
        
        elif self.current_command.startswith("@"):
            return CommandType.A_COMMAND
        
        return CommandType.C_COMMAND

    def symbol(self) -> str:
        """
        Called only when `command_type() -> A_COMMAND | L_COMMAND`.
        Parses the symbol or value of the `current_command` the "Xxx" or "(Xxx)" or "@Xxx".
        :returns: The symbol/decimal value of the current command.
        """
        ALLOWED_CHARS = ('_', '.', '$', ':')  # Specified allowed symbols in addition to alphanumerals.
        sym = ""  # Symbol string will be populated.
        is_decimal = False  # Starting assumption, correct later.

        for char in self.current_command:
            # Skip @ and ().
            if char in ['@', '(', ')']:  continue

            # Assume it will be a decimal value.
            if char.isnumeric() and len(sym) == 0:  
                is_decimal = True

            # Final validation.
            if not is_decimal and (char in ALLOWED_CHARS or char.isalnum()):
                sym += char
            
            elif is_decimal and char.isdecimal():
                sym += char

            # If character is not allowed, raise error.
            else:  raise ParseError(f"Invalid character in symbol or value on line {self.current_line}.", char)
        
        return sym


    def dest(self) -> str:
        """
        Called only when `command_type() -> C_COMMAND`.
        :returns: The `dest` mnemonic (A, AM, DM, AMD, etc...).
        """

    def comp(self) -> str:
        """
        Called only when `command_type() -> C_COMMAND`.
        :returns: The `comp` mnemonic (0, 1, -1, D, A, !A, etc...)
        """

    def jump(self) -> str | None:
        """
        Finds and parses the `jump` mnemoic of the current C command.
        Called only when `command_type() -> C_COMMAND`.
        :returns: The `jump` mnemonic (JMP, JLE, JGT, etc...)
        """
