def reverseKeysValue(fruit_dictionary):
    newDict = {}
    keyList = list(fruit_dictionary.keys())
    valueList = list(fruit_dictionary.values())

    newDict = dict(zip(valueList, keyList))
    return newDict
    

def main():
    fruit_dictionary = {'apples':2,'pears':4,'bananas':8,'kiwi':10}
    print (fruit_dictionary)
    print (reverseKeysValue(fruit_dictionary)) 
        
main()