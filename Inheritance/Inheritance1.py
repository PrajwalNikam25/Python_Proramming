

class Parent:

    def __init__(self):
        print("In parent Constructor")
        self.x =10;
        self.y =20

    def dispData(self):
        print(self.x)
        print(self.y)

class Child(Parent):
    pass

obj = Child()
obj.dispData()
