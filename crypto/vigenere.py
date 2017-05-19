from helpers import alphabet_position, rotat_character

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
    vig_encrypt(input("Give me a string:"), input("And a key:"))
 #   testEqual(vig_encrypt("The crow flies at midnight!", 'boom'), 'Uvs osck rmwse bh auebwsih!')



if __name__ == "__main__":
    main()
