

class Parent:

    z = 30

    @classmethod
    def parentData(cls):
        print(cls.z);

    def __init__(self):
        print("In constructor")
        self.x = 10
        self.y = 20

    def printData(self):
        print(self.x)
        print(self.y)

    def __del__(self):
        print("In destructor")

obj = Parent()
obj.printData()
Parent.parentData()
obj.__del__()
del obj
