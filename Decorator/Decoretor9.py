

def decoretorFun(func):

    def wrapper():

        print("In wrapper start")
        func()
        print("In wrapper End")
    return wrapper

def decoretorRun(func):

    def wrapper():
        print("In wrapper 2")
        fun()
        print("In wrapper end 2")

    return wrapper

@decoretorFun
@decoretorRun

def normalFun():
    print("In normal Fun")


normalFun()
