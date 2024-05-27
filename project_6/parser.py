from enum import Enum


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
        self.current_command = ""

    def hasMoreCommands(self) -> bool:
        """
        Checks if there are more commands in the input file to parse.
        :return: True if there are more lines to parse.
        """

    def advance(self) -> None: 
        """
        Called only if `hasMoreCommands` is true.
        Reads from input and sets the new `current_command`.
        """

    def commandType(self) -> CommandType:
        """
        Parse the `CommandType` of `current_command`.
        :returns: A `CommandType` enum describing the current command.
        """

    def symbol(self) -> str:
        """
        Called only when `commandType() -> A_COMMAND | L_COMMAND`.
        :returns: the symbol/decimal value of the current command.
        """

    def dest(self) -> str:
        """
        Called only when `commandType() -> C_COMMAND`.
        :returns: The `dest` mnemonic (A, AM, DM, AMD, etc...).
        """

    def comp(self) -> str:
        """
        Called only when `commandType() -> C_COMMAND`.
        :returns: The `comp` mnemonic (0, 1, -1, D, A, !A, etc...)
        """

    def jump(self) -> str | None:
        """
        Finds and parses the `jump` mnemoic of the current C command.
        Called only when `commandType() -> C_COMMAND`.
        :returns: The `jump` mnemonic (JMP, JLE, JGT, etc...)
        """
