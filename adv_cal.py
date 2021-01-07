def cal(num1,num2,op):
    if op=="+":
        print(num1+num2)
    elif op=="-":
        print(num1-num2)
    elif op == "/":
        print(num1 / num2)
    elif op=="%":
        print(num1%num2)
    elif op=="*":
        print(num1*num2)
    else:
        print("invalid operation")


x=float(input("enter ist number"))
y=float(input("enter 2nd number"))
z=input("enter the operator")

cal(x,y,z)