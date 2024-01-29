

list = [10,"Prajwal",20,"Nikam",40]

print("Start code")

try:

    index1 = int(input("Enter index1 :"))
    index2 = int(input("Enter index2 :"))
    add = list[index1] + list[index2]

except ValueError as err:
    print("Enter Valid int")
except IndexError as err:
    print("Enter valid Index")
except TypeError as err:
    print("Enter correct index")
else:
    print(add)
