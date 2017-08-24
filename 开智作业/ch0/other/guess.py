from random import randint
YourAnswer = 0
Guess = randint(0,20) 
j = 10
i = 0
print("Now let's guess the numnber between 0 to 19")
while i <10 and  Guess != int(YourAnswer):
    print("Come on you have %d times" %j)
    YourAnswer = input("please input your answer:")
    if int(YourAnswer)-Guess >0:
    	print("Bigger!")
    elif int(YourAnswer)-Guess <0:
    	print("Smaller!")
    else:
    	print("Biggo ,that's right!")
    i += 1
    j -= 1
    
if Guess == int(YourAnswer):
	print("Congratulaitions,your are the winner")
else:
	print("I'm sorry for your missing the answer")
    