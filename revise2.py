secret= "py"
guess=""
count=0
limit=3
ofg=False

while guess!=secret and  not (ofg):
    if count<limit:
        print(count,"out of 3 guesses")
        guess=input("enter the answer")
        count+=1
    else:
        ofg=True

if ofg:
    print("you lose")
else:
    print("you win")
