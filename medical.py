medical = "Yes"
answer = "No"

print("=================================================================")
print("WELCOME TO YOU WILL NOT DIE HERE HOSPITAL...AMEN")
print("=================================================================") 

name = str(input("KINDLY ENTER YOUR NAME, FOR A USER FRIENDLY INTERFACE: "))

medical = str(input("WHAT IS YOUR PROBLEM: "))
answer = str(input("HAVE YOU HAD THIS PROBLEM BEFORE(Yes or No):" ))
if answer == "yes":
		print("WELL, YOU HAVE IT AGAIN...\t" + name)
elif answer == "no":
   print("WELL YOU HAVE IT NOW..\t" + name)