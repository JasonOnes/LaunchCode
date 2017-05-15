from test import testEqual

def translate(text):
    eng2pir = { "sir" :	"matey",
            "hotel" :	"fleabag inn",
            "student" : 	"swabbie",
            "boy" :	"matey",
            "madam" :	"proud beauty",
            "professor" :	"foul blaggart",
            "restaurant" :	"galley",
            "your" :	"yer",
            "excuse" :	"arr",
            "students" :	"swabbies",
            "are" :	"be",
            "lawyer" :	"foul blaggart",
            "the" :	"th’",
            "restroom" : "head",
            "my" : "me",
            "hello" : "avast",
            "is" :	"be",
            "man" 	: "matey"}
    text = text.split()
    
    pirate_speak = ""

    for word in text:
        if not word[-1].isalpha():

            pirate_speak += eng2pir.get(word[:-1], word) + word[-1]+  " "
        else:
            pirate_speak += eng2pir.get(word, word) + " "
    pirate_speak = pirate_speak[:-1]
    #print(pirate_speak)
    return pirate_speak




text = "hello my man, please excuse your professor to the restroom!"
testEqual(translate(text), "avast me matey, please arr yer foul blaggart to th' head!")
#print(translate("Get theee out of this restaurant dumb students"))
print(len(translate("hello my man, please excuse your professor to the restroom!")))
print(len(translate(text)))
print(len("avast me matey, please arr yer foul blaggart to th' head!"))
print(type(translate(text)))
print(type("avast me matey, please arr yer foul blaggart to th' head!"))
a = list("avast me matey, please arr yer foul blaggart to th' head!")
b = list(translate(text))
x = [i for i in a if i not in b]
y = [i for i in b if i not in a]
print(x)
print(y)
