

class Parent:

    z =30;
    def __init__(self):

        self.x =10
        self.y =20

    def printData(self):

        print(self.x)
        print(self.x)

    def __del__(self):
        print("In Destructor")

    @classmethod
    def parentData(cls):
       print(cls.z)

class Child(Parent):

    pass

obj = Child();
obj.printData()
Parent.parentData()
