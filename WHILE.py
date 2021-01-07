#creating while loop
i=1
while i<5 :
    print("hi")
    i=i+1

print("while loop executed")
print("")
print("")
print("")
#a basic guessing game

secret_wor= "python"
gues=input("Enter my favorite programming language")
while gues!= secret_wor :
    gues=input("Enter my favorite programming language")

print("YOU win", "answer is ",gues)
print("")
print("")
print("")
#creating a guessing game with limit
print("Welcome To The Great Guessing Game")
guess=""
secret_word="python"
guest_count=0   #no of times the user entered the guess
guess_limit=3   #the max. limit for input
out_of_guess= False  #if user is out of guess or not

while guess != secret_word and not (out_of_guess) :
    if guest_count < guess_limit :
        guess= input("Enter my favorite programming language")
        guest_count +=1
    else:
        out_of_guess= True

if  out_of_guess:
    print("You are out of guess.Try later!")
else:
    print("You win.The correct answer is ",guess)