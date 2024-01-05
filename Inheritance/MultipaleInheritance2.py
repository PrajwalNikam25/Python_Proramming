

class Parent1:

    def __init__(self):

        self.x = 10
        self.y = 20

    def run(self):

        print("In run")
        print(self.x)
        print(self.y)

class Parent2:

    def __init__(self):

        self.a = 30
        self.b = 40

    def fun(self):

        print("In fun")
        print(self.a)
        print(self.b)

class Child(Parent1,Parent2):
    a = 30
    b = 40

obj = Child()
obj.run()
obj.fun()

