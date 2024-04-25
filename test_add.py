from add import add

def test_add_function():
	assert add(1, 5) == 6
	assert add(10, 11) == 21

def test_add_strings():
	assert add("james", "man") == "james man"
	assert add("mary", "work") == "mary work"

def test_negative_value_with_add_function():
	assert add(-9, -2) == 11