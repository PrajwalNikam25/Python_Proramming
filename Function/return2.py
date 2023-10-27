


def addByTen(a,b,c):

    a += 10
    b += 10
    c += 10

    return a,b,c

x = addByTen(10,20,30)

print(type(x))

print(x)

p,q,r = addByTen(10,20,30)

print(p)
print(q)
print(r)

print()
for i in x:
    print(i)
    

