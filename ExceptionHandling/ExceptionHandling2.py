

list = [10,"Prajwal",20,"Shreya",30]

try:

    index1 = int(input("Enter num :"))
    print(list[index1])
    index2 = int(input("Enter num :"))
    print(list[index2])
   
    add = list[index1] + list[index2]

except:
    print("Exception d")
else:
    print(add)



