#!/usr/bin/env python
"""
Assembler's driver file.
"""
from pathlib import Path
import sys

import asm_code as c
from asm_parser import Parser, CommandType 
from symbolic_table import SymbolicTable


IN_PATH = Path(sys.argv[1])

# Be safe!
if not IN_PATH.is_file():
    raise FileNotFoundError("File not found:", IN_PATH.absolute)

OUT_PATH = IN_PATH.parent.joinpath('./' + IN_PATH.name.replace(".asm", ".hack"))


def first_pass() -> SymbolicTable:
    """
    Runs the first pass over the given file, returning the necessary symbolic table for compilation.
    :returns: A symbolic table populated with the appropriate values.
    """
    print("First pass...")

    parser = Parser(IN_PATH)
    table = SymbolicTable()

    while parser.hasMoreCommands():
        parser.advance()

        # Only act on pseudocommands.
        if parser.command_type() != CommandType.L_COMMAND:
            continue

        if parser.current_command[0] + parser.current_command [-1] == "()":
            table.add_entry(parser.symbol(), parser.line_idx)

    return table


def second_pass(table: SymbolicTable) -> list[str]:
    """
    Runs the second pass over the given file, and returns the lines to print to file.
    """
    out_lines = []
    parser = Parser(IN_PATH)

    while parser.hasMoreCommands():
        parser.advance()
        print(parser.current_command)

        # Handle C-commands.
        if parser.command_type() is CommandType.C_COMMAND: 
            dest = c.dest(parser.dest())
            comp = c.comp(parser.comp())
            jump = c.jump(parser.jump())
            out_lines.append(f"111{dest}{comp}{jump}")

        # Handle other commands -- only appending if A-command.
        else:
            symbol = parser.symbol()
            out_lines.append(f"0{symbol}")

        print(out_lines[-1])
    
    return out_lines
    

def main() -> None:
    """
    Runs the parsing process, printing each line to file.
    """
    parser = Parser(IN_PATH)

    table = first_pass()
    out_lines = second_pass(table)

    # Then save to file...


if __name__ == "__main__":
    main()
