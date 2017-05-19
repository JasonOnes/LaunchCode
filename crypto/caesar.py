from helpers import alphabet_position, rotat_character

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


