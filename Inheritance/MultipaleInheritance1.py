
class Parent1:

    def disData(self):

        print("In Parent 1")

class Parent2:

    def printData(self):

        print("Print Data")

class Child(Parent1,Parent2):
    pass


obj = Child()
obj.disData()
obj.printData()
