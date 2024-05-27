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
        if char not in "AMD":  raise CodeError(f"Unexpected character in 'dest' token: {char}")

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



def jump(mnemonic: str) -> str: 
    """
    Translates the `jump` mnemonic string to a string of 3 bits.
    :returns: 3 bits as a string.
    """
    
