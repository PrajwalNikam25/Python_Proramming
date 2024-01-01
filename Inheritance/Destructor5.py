


class Parent:

    def __init__(self):

        print("In Constructor")

    def __del__(self):

        print("In destructor")

def fun():

    print("Start")
    obj = Parent()
    print("End")

fun()
print("End Code")
