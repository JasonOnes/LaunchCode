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

def vig_encrypt(text, word):
    if len(text) > len(word):
        x = len(text) // len(word)
        y = len(text) % len(word)
        cipher_list1 = word * x
        cipher_list = cipher_list1 + cipher_list1[:y]
    elif len(text) == len(word):
        cipher_list = word
    elif len(text) < len(word):
        cipher_list = word[:len(text)]
    idx_list = []
    for char in cipher_list:
        idx_list.append(alphabet_position(char))
    encrypt_list = ""
    i = 0
    for letter in text:
        if letter == " ":
            encrypt_list += " "
        else:
            encrypt_list += rotat_character(letter, idx_list[i])
            i += 1
    print(encrypt_list)
    return encrypt_list

def main():
    vig_encrypt("The crow flies at midnight!", 'boom')
    vig_encrypt("W       3   a", 'bc')
    vig_encrypt("AAAAAAAAAaaaaaaaaaaaaa", 'nally')
    vig_encrypt("EEEEEEEEEEEEeeeeeeeeeeeee", 'nally')
    vig_encrypt("helLO", 'I don\'t like Mondays!')




if __name__ == "__main__":
    main()
