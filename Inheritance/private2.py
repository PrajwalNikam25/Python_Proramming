


class Parent:

    __t = 50

    def __init__(self):
        self.x = 10;
        self.__y = 20;

    def __fun(self):
        print("In fun")

class Child(Parent):

    def printData(self):
        print(self.x)
        print(self._Parent__y)

print(dir(Parent))

obj = Child()

obj.printData()

print(dir(obj))

print(Parent._Parent__t)



