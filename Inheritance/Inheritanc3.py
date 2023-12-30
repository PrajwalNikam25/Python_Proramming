

class Parent:

    def __init__(self):

        print("In constructor Parent")
        self.x = 10;
        self.y =20;

    def dis(self):

        print(self.x)
        print(self.y)

class Child(Parent):

    def __init__(self):

        print("In constructor Child")
        
        super().__init__()
        self.x =30
        self.y=40

obj=Child()
obj.dis()


