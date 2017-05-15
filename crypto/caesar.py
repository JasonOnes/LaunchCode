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

def encrypt(text, rot):
    """ Uses the rot encryption for each character to return an encoded string"""
    new_text = ""
    for char in text:
        new_text += rotat_character(char, rot)
    return new_text 


def main():
    print(encrypt(input("Type a message: "), int(input("Rotate by: "))))
    print(alphabet_position("A"))
    print(rotat_character("A", 2))
    print(encrypt("1837- 9934 jasjdoiKhYFdDoasnv", -9))


if __name__ == "__main__":
    main()


