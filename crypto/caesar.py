from helpers import alphabet_position, rotat_character
#from sys import argv

def encrypt(text, argv):
    """ Uses the rot encryption for each character to return an encoded string"""
    #rot = argv
    new_text = ""
    for char in text:
        new_text += rotat_character(char, argv)
    return new_text 


def main():
    from sys import argv

    #print("This is what the user typed on the command line:", argv)
    
    print(encrypt(input("Type a message: "), int(input("Rotate by: "))))
    # print(alphabet_position("A"))
    # print(rotat_character("A", 2))
    # print(encrypt("1837- 9934 jasjdoiKhYFdDoasnv", -9))
    #print(encrypt(input("Please type a message: "), argv))

if __name__ == "__main__":
    main()


