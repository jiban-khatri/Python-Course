# == While Loop ==
num = int(input("enter number: "))
i = 1
while i<=10:
    print(f"{num} * {i} = {num*i}")
    i+=1



gameNum = 14
guessCount = 1
userNum = int(input("Guess a number between 1 - 100"))
while userNum != gameNum:
    userNum = int(input("Guess a number between 1 - 100"))
    guessCount+=1
else:
    print("You guessed it correctly in", guessCount,"rd time")





# =========== For Looop ========

name = "jiban"
for i in name:
    print(i)



for i in range(1,11):
    print(i)


for i in range(1,21,3):
    print(i)


for i in range(10,0,-1):
    print(i)



curr_popn = 10000

for years in range(10,0,-1):
    print(i, curr_popn)
    curr_popn = curr_popn - 0.1*curr_popn