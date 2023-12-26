


def Outter():

    print("In Outter")

    def Inner1():

        print("In Inner1")

    def Inner2():

        print("In Inner2")

    return Inner1,Inner2

ret1,ret2 = Outter()

ret1()
ret2()
