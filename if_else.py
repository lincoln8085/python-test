
def number(x):
    if x%2== 0:
        print(x,"is even")
    elif x%2==1:
        print(x,"is odd")
    else:
        print("you entered a wrong number")
    return x

y=input("enter the number to check whether even or odd")
number(int(y))

#just a try with boolean
even= False
odd= False
if even:
   print("is even")
elif not(odd):
    print("is odd")
else:
    print("you entered a wrong number")