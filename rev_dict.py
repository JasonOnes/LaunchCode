def reverse_dict(dict_name):
    reverse_dict = {tuple(v):k for k, v in dict_name.items()}
    return reverse_dict

adict = {1:"one", 2:"two", 3:["three", "four", "five"]}
bdict = {k : v for k,v in enumerate("Hello cruel world!")}

if __name__ == "__main__":

    print(reverse_dict(adict))
    print(reverse_dict(bdict))
