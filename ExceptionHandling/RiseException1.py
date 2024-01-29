

def Voting(name,Age):

    if(Age < 18):

        raise ValueError("Age is not valid")
    else:
        print("Congratulation you are Voter")

name = input("Enter Your Name :")

try:

    Age = int(input("Enetr Youer Age : "))
except:
    print("Enter Valid Age")
    Age = int(input("Enetr Youer Age"))


Voting(name,Age)







