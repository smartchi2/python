def factorial(n):
	fact = 1
	for index in range(1,n+1):
		fact = fact * index
	return fact


number = int(input("Enter factorial:  "))
fact = factorial(number)
print(fact)
