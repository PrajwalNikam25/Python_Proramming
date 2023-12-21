

def run():

    print("In run")

def fun(x):

    x()
    print("In fun")

fun(run)
