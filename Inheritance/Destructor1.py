

class Parent:

    z = 30;

    def __init__(self):

        print("In Parent Constructor")
        self.x = 10;
        self.y= 20;

    def disData(self):
        print(self.x)
        print(self.y)

    @classmethod
    def disParent(cls):
        print(cls.z)
    
    def __del__(self):
        print("In Del");

obj1 = Parent()
obj1 = Parent()

print("Code End")
