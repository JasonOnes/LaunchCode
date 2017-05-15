

def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    new_name = fullname.split()
    initials = ''
    for name in new_name:
        initials += name[0].upper()
    return initials


def main():
    """ Just to execute dunder name dunder main"""
    print(get_initials("jason jones"))
    get_initials("Julie ann Moore")
    print(get_initials(input("What is your full name?")))

if __name__ == '__main__':
    main()
    