import random

Lucky_Number  = random.randrange(1, 10)


print("===========================================================================================================")
print("WELCOME TO GOD PUNISH YOU IF YOU NO WIN Lucky Number....")
print("===========================================================================================================")

sum = 0;
win = 0;
Number = 0;

#print(Lucky_Number)
while(Number != Lucky_Number):
	Number = int(input(" Enter Lucky  number to win : "))
	sum = sum + 1
print("FINAL RESULT OF YOUR GAME PLAYED, CHECK BELOW TO SEE")
if(Number == Lucky_Number):
		print("you have won our Lucky Bet by", + Number)
if(Number != Lucky_Number):
		print("You did not win try again or logout by", + sum)
elif(Number == 0):
		print("Thanks for betting with God punish you if you no win bet by", Number)

print("Your total tried numbers are", sum)
