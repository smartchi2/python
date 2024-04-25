def add_ing(input:str):
	added = "ing"
	size = len(input)
	if size >=3:
		return input+added
	else :
		return input


age = "ca"
print(add_ing(age))