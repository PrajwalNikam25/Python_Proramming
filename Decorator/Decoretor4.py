

def run():

    print("In run")

def fun(x):

    print("In fun")
    x()

def gun(y):

    print("In gun")
    y()


fun(run)
