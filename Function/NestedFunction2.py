

def Outter():

    def Inner1():

        print("In Inner Function 1")

    def Inner2():

        print("In Inner Function 2")

    Inner1()
    Inner2()
    print("In Outter Function")


Outter()


