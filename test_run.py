#print a list using various methods

num=[10,20,30,40]
#using normal function
print("using print only")

print(num[1])
print(num[2])
print("")
#using for loop
print("using for loop")
for element in num:
    print(element)

print("")
#using function

print("")
 #using while loop
print("using while loop")
count=0
while count<len(num):
     print(num[count])
     count+=1
print("")