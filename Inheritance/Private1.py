

class Parent:

    z =30

    def __init__(self):
        self.x = 20
        self.__y = 40

print(dir(Parent))
obj = Parent()
print(dir(obj))
