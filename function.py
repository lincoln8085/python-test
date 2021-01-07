def user(name,pswd):
    print("Welcome to AAT")
    print("your username is "+ name,"and password is", pswd)

def user1(name,pswd):
    return name,pswd

print("please login")
x=input("Please enter usernme")
y=input("please enter password")
user(x,y)
print("   "
      "   "
      "  ")
print("Your details are", user1(x,y))
print("   "
      "   "
      "  ")
def sq(num):
    print("this is a square function")
    return num*num

x = input("enter the number to square")
y= sq(int(x))
print(y)
print("   "
      "   "
      "  ")
def student(name,roll_no):
    w=name.upper()
    print("Your name is "+w)
    print("your roll no is ", roll_no)
    return roll_no*roll_no- 1

x= input("enter your name ")
y= input("enter your roll no")

a= student(x,int(y))
print("Your ID NO. is ",a)

print("   "
      "   "
      "  ")

def corona(active,recover):
    print("Current active cases are ",active)
    print("Current recovered cases are ",recover)
    print("The total count of corona +ve cases", active+recover)
    return active+recover* 10-100/2

x=input("Enter the number of active cases")
y=input("Enter the number of recovred cases")

target=corona(int(x),int(y))
print("The future forcasted target for corona +ve cases are ",int(target))
