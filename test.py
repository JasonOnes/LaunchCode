def testEqual(output, expected_out):
    if output == expected_out:
        print("Pass")
        return True
    else:
        print("Wanted this: ", expected_out)
        print("Got this crap: ", output)
        print("Fail")
        return False
