def get_trimmed_string(str):

	if len(input_str) < 2:
		return""
	else:
		return  str[2:-2]
input_str = "semicolon"
result = get_trimmed_string(input_str)
print(result)
