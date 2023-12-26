


def Decoretor(func):

    print("In Decoretor")

    def wrapper(*args):

        print("start")
        val = func(*args)
        print("End")

        return val
    return wrapper

@Decoretor
def normalFun(x,y):

    print("In NormalFun")

    return x + y

normalFun(10,20)
