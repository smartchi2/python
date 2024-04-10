pass_mark = 45
total_pass = 0
total_failed = 0
count = 0
for grade in range (15):
	grade = int(input("Enter scores: "))

	if grade >= pass_mark:
		total_pass += 1

	if grade < pass_mark:
		total_failed += 1
	
	count =+ 1

#average = total_pass / 15
#average = total_failed / 15
print(f"total passed students is {total_pass}")
print(f"total failed students is {total_failed}")

 
 
