


class VotingError(Exception):

    def __init__(self,msg):
        super().__init__(msg)

def voting(name,age):

    if(age < 18):
        raise VotingError("Your age is not valid")
    else:
        print("Congratulations")

print("Start Code")

name = input("Enter your name :")

try:
    age = int(input("Enter your age :"))
except:
    print("Enter Valid age")
    age = int(input("Enter your age"))

try:
    voting(name,age)
except VotingError as err:
    print(err)
