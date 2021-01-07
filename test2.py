x=input("enter the number and  ")
y=input("the power")

result=1

for i in range(int(y)):
    result= result*int(x)



print(result)


#using function

def exp(num, pow):
    res= 1
    for i in range(pow):
        res= res*num
    return res

a= input("enter the number ")
b=input(" enter the power to be raised to ")

r= exp(int(a),int(b))
print(r)