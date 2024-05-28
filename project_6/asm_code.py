#!usr/bin/env python
"""
This module translates Hack into binary code.
"Bits" are written as strings, as they ultimately will be written to a file as symbols. (right?)
"""

from errors import *


def dest(mnemonic: str) -> str:
    """
    Translates the `dest` mnemonic string to a string of 3 bits.
    :param mnemonic: The mnemonic to translate. Expects "A", "M", "D", or some combination.
    :raises CodeError: If the mnemonic is not as expected. 
    :returns: 3 bits as a string.
    """
    # Initial destination information.
    dest_a = False
    dest_m = False
    dest_d = False

    for char in mnemonic:
        # Raise error on unexpected character.
        if char not in "AMD":  raise CodeError(f"Unexpected character in 'dest' token: '{char}'")

        # Simple repetition.
        dest_a = dest_a or char == "A"
        dest_m = dest_m or char == "M"
        dest_d = dest_d or char == "D"  # Note that this method allows for "AAAAAAAAAAAAAAA" and "MMMMM" and "AMDMDMMD" to be valid tokens. 

    return ''.join([str(int(dest)) for dest in (dest_a, dest_d, dest_m)])


def comp(mnemonic: str) -> str:
    """
    Translates the `comp` mnemonic string to a string of 7 bits.
    :returns: 7 bits as a string.
    """
    def get_bits() -> str:
        """ Massive switch statement to return the 6 c-bits. """
        match mnemonic:
            case '0':  return '101010'
            case '1':  return '111111'
            case '-1':  return '111010' 
            case 'D':  return '001100'
            case 'A' | 'M':  return '110000'
            case '!D':  return '001101'
            case '!A' | '!M':  return '110001'
            case '-D':  return '001111'
            case '-A' | '-M':  return '110011'
            case 'D+1':  return '011111'
            case 'A+1' | 'M+1':  return '110111'
            case 'D-1':  return '001110'
            case 'A-1' | 'M-1':  return '110010'
            case 'D+A' | 'D+M':  return '000010'
            case 'D-A' | 'D-M':  return '010011'
            case 'A-D' | 'M-D':  return '000111'
            case 'D&A' | 'D&M':  return '000000'
            case 'D|A' | 'D|M':  return '010101'

        # If none matched:
        raise CodeError(f"Comp token '{mnemonic}' could not be interpreted.")
        
    # Concatenate a-bit status beside `get_bits()` result
    return f"{int('M' in mnemonic)}{get_bits()}"


def jump(mnemonic: str) -> str: 
    """
    Translates the `jump` mnemonic string to a string of 3 bits.
    :returns: 3 bits as a string.
    """
    match mnemonic:
        case '':  return '000'
        case 'JGT':  return '001'
        case 'JEQ':  return '010'
        case 'JGE':  return '011'
        case 'JLT':  return '100'
        case 'JNE':  return '101'
        case 'JLE':  return '110'
        case 'JMP':  return '111'

        case _: 
            raise CodeError(f"Jump token '{mnemonic}' could not be interpreted.")
        