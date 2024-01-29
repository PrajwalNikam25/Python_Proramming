
class VotingError(Exception):
    def __init__(self,msg ):
        super().__init__(msg)

def voting(name,age):

    if(age < 18):
        raise VotingError("Your age is not valid")
    else:
        print("Congratulations")

print("Start Code")
try:
    age = int(input("Enter Your age :"))
except:
    print("Age is Not valid")
    age = int(input("Enter Your age :"))

name = input("Enter Your name :")

try:
    voting(name,age)

except VotingError as err:
    print(err)

print("End Code")




