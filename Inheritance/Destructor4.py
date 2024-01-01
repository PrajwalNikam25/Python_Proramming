


class Parent:

    def __init__(self):

        print("In constructor")

    def __del__(self):

        print("In Destructor")

obj1 = Parent()
obj2 = Parent()

obj3 = obj1

del obj1

print("End Code")
