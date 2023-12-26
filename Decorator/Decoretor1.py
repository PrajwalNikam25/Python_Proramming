


def Outter():

    print("In Outter Function")

    def Inner1():

        print("In Inner1")

    def Inner2():

        print("In Inner2")
    
    Inner1()
    Inner2()

Outter()
