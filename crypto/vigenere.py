from helpers import alphabet_position, rotat_character

def encrypt(text, word):
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
        elif letter.isalpha():
             encrypt_list += rotat_character(letter, idx_list[i])
             i += 1
            #encrypt_list += letter
        else:
            encrypt_list += letter
            #encrypt_list += rotat_character(letter, idx_list[i])
            #i += 1
    print(encrypt_list)
    return encrypt_list

def main():
    # encrypt("The crow flies at midnight!", 'boom')
    # encrypt("W       3   a", 'bc')
    # encrypt("AAAAAAAAAaaaaaaaaaaaaa", 'nally')
    # encrypt("EEEEEEEEEEEEeeeeeeeeeeeee", 'nally')
    # encrypt("helLO", 'I don\'t like Mondays!')
    # encrypt(input("Give me a string:"), input("And a key:"))
    #encrypt("The crow flies at midnight!", 'boom'), 'Uvs osck rmwse bh auebwsih!')
    encrypt('a', 'a')
    encrypt('Sailing <3 ships thru br0ken harbors', 'NeilYoung')
    encrypt("Ailin lakjfl jjj", "hello cruel world")

if __name__ == "__main__":
    main()
