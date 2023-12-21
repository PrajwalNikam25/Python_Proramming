



def decorator(func):

    def wrraper():
    
        print("In Start")
        func()
        print("In end")

    return wrraper


def funNode():
    print("In fun")

funNode = decorator(funNode)
funNode()
