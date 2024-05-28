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

        table.add_entry(parser.symbol(), parser.line_idx)
        print(parser.line_idx)

    return table


def second_pass(table: SymbolicTable) -> list[str]:
    """
    Runs the second pass over the given file, and returns the lines to print to file.
    """
    out_lines = []
    parser = Parser(IN_PATH)

    while parser.hasMoreCommands():
        parser.advance()

        match parser.command_type():
            # Handle C-commands.
            case CommandType.C_COMMAND: 
                dest = c.dest(parser.dest())
                comp = c.comp(parser.comp())
                jump = c.jump(parser.jump())
                out_lines.append(f"111{comp}{dest}{jump}")

            # Handle A-commands.
            case CommandType.A_COMMAND:
                symbol = parser.symbol()

                # If decimal, literal. Else check if it exists and auto-populate if not.
                if symbol.isdecimal():
                    value = int(symbol)
                
                elif not table.contains(symbol):
                    table.add_entry(symbol, None)

                # If not decimal, get value.
                if not symbol.isdecimal(): 
                    value = table.get_address(symbol)

                # Generate binary and output.
                binary = bin(value)[2:].zfill(15)[-15:]  # Truncate
                out_lines.append(f"0{binary}")
    
    return out_lines
    

def main() -> None:
    """
    Runs a two-pass parsing routine, then prints the results to file.
    """
    print(f"Parsing '{IN_PATH}'...")

    print("First pass...")
    table = first_pass()

    print("Second pass...")
    out_lines = second_pass(table)

    
    # Then save to file...
    print(f"Saving to '{OUT_PATH}'") 
    with open(OUT_PATH, 'w') as fp:
        fp.writelines([l + '\n' for l in out_lines])


if __name__ == "__main__":
    main()
