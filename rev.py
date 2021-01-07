def fun (num):
    print(num*num)

def f(n):
    return n*n

x=input("enter a value to square")

fun(int(x))
y=f(int(x))

print(y)

#case

def idgen(name,roll):
    U=name.upper()
    print("name is ",U)
    print("your roll no is ",roll)
    return roll*roll-2

nm=input("enter yout name")
ro=input("enter your roll no")

y= idgen(nm,int(ro))

print("your ID is as follows:",y)