
#12jan21
#for loop
for i in "sam":
    print(i)

print("")

list=["ktm","benelli","bmw"]
for i in list:
    print(i)

print("")

#sum
num=[12,23,15]
sum=0
for i in num:
    sum+=i

print(sum)
print("")

#range()
for i in range(4):
    print(i)

print("")

for i in range(1,6):
    print(i)

print("")

x=input("enter range ")
for i in range(int(x)):
    print(i)


print("")

#print a list using len and range
for i in range(len(list)):
    print(list[i])

print("")

#if_else in for
for i in range(6):
    if i==0:
        print("for loop starts")
    else:
        print(i,"th iteration")

print("")

#using maths
print("welcome to square a number")
x= input("enter the number ")
y=input("enter the power")
power=1
for i in range(int(y)):
    power=power*int(x)

print(int(power))
print("")

#using function for maths
def exp(num,pwr):
    power=1
    for i in range(pwr):
        power=power*num

    return power

x= input("enter the number ")
y=input("enter the power")
q=exp(int(x),int(y))
print(int(q))

print("")
