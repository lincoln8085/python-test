#example_1
for identifier in "name":
    print(identifier)
print("")

#example_2
name=["hi","bye"]
for element in name:
    print(element)
print("")

#example_3
num=[10,23,34]
sum=0
for i in num:
    sum=sum+i

print(sum)
print("")

#using_range()_in_for_loop
for i in range(5):
    print(i)
print("")

for i in range(2,6):
    print(i)
print("")

x=input("enter the range to print")
for i in range(int(x)):
    print (i)
print("")

for i in range(len(num)):
    print(num[i])
print("")

y=input("enter the range :")
for i in range(int(y)):
    if i==0:
        print("for loop starts")
    else:
        print(i,"th iteration")