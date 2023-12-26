

def decoretor(func):

    def wrapper():

        print("Start")
        func()
        print("End")

    return wrapper

def normalFun():

    print("In normal Fun")

normalFun = decoretor(normalFun)
normalFun()
