# 5th jan2021

i = True
# if changes universal value of var
if i:
    i = False
    print(i)
else:
    i = True
    print(i)

print(i)
# increment in while loop
i = 1

while i < 5:
    print(1)
    i += 1
    print(i)

print(i)


#11jan21

#ist way
guess=""
se="log"
print("welcome to guess game ")
while   guess!=se:
    guess=input("enter sec word ")
    if guess!=se:
        print("oops!incorrect answer.try again")
    else:
        print("voila! good guess")

print("your guess is correct, answer is : ",guess)

#2nd way

guess=""
secret_word="python"
count_limit=3
count=0
out_of_guess= False

print("GAME START,You have 3 guesses ")
while guess!=secret_word and not(out_of_guess):
    if count<count_limit:
        guess=input("enter the secret word.guess it ")
        count+=1
        print(count, " guess over ")

    else:
        out_of_guess=True

if out_of_guess:
    print("your are out of guess. you lose")
else:
    print("voila. you are a champion. you win ")
