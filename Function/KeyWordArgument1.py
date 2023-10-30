

def fun(**args):

    print(args)

    for key,value in args.items():
        print(key,value)

fun(a=10,b=20,c=30,d=40)
