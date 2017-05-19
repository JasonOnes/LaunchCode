""" These functions provide the building blocks of the rotation method of ecryption."""


def alphabet_position(letter):
    """ Returns an index number for any letter in the alphabet"""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    idx = alpha.find(letter)
    return idx

def rotat_character(char, rot):
    """ Returns a character encoded by index position relative to rot"""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        idx = alphabet_position(char)
        new_idx = (idx + rot) % 26
        if char.isupper():
            rot_char = alpha[new_idx].upper()
        else:
            rot_char = alpha[new_idx]
    else:
        rot_char = char
    return rot_char