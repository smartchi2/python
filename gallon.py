gallon = 0
miles = 0
total_miles = 0
stoper = 0
print("==============================================================")

print("WELCOME TO SMART CHI AUTOS")	
print("==============================================================")
while stoper != -1:
	gallon = int(input("Enter gallon used (-1 to end): "))
	miles = int(input("Enter miles driven: "))
	total_miles = miles / gallon
	#print(f"The miles of tankful divided by gallon is {total_miles:.2f}")
	stoper = int(input(" press -1 to stop or Enter 2 to continue : "))
	print(f"The miles of tankful divided by gallon is {total_miles:.2f}")
	

