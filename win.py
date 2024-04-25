


print("WELCOME TO GOD PUNISH YOU IF YOU NO WIN Lucky Number....")

sum = 0;
win = 0;
for win in range(3):
	Lucky_Number = int(input(" Enter Lucky  number three times to win : "))
	
	sum += Lucky_Number
	if(Lucky_Number <= 10):
		print("you have won our Lucky Bet by", + win)

	if(Lucky_Number > 10):
		print("You did not win try again or logout by", + win)

	elif(Lucky_Number == 0):
		print("Thanks for betting with God punish you if you no win bet by", Lucky_Number)

print("Your total tried numbers are", sum)


		

