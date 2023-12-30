


class Parent:

    z =30;

    @classmethod
    def classParent(cls):
        print(cls.z)

    def __init__(self):

        print("In parent Constuctor")
        self.x=10
        self.y=20

    def disData(self):
        print(self.x);
        print(self.y);

class Child(Parent):
    pass

obj = Child()
obj.disData()
obj.classParent()
