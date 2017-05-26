def reverse_dict(dict_name):
    # for v in dict_name.items():
    #     print(type(v))
    #     if  type(v) == list:
    #         reverse_dict = {tuple(v):k for k, v in dict_name.items()}
    #     else:
    #         reverse_dict = {v:k for k, v in dict_name.items()}
    reverse_dict = {tuple(v):k for k, v in dict_name.items()}
    return reverse_dict

adict = {1:"one", 2:"two", 3:["three", "four", "five"]}
bdict = {k : v for k,v in enumerate("Hello cruel world!")}
fruit_dictionary = {'apples':'2','pears':'4','bananas':'6','kiwi':'10'}
cdict = {'apple': 2, 'pears': 4, 'bananas': 6, 'kiwi':10}

def test_key():
    assert dict.keys() == type(str)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(reverse_dict(adict))
    print(reverse_dict(bdict))
    print(reverse_dict(fruit_dictionary))
    print(reverse_dict(cdict))

    
