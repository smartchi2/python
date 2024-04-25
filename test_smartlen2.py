from smartlen2 import add

def test_add_function():
	assert add(10, 20) == 30
	assert add(100, 50) == 150

def test_add_strings():
	assert add("smart", "power") == "smart power"
	assert add("eniola" "job") == "eniola job"


def test_negative_values_with_add_function():
	assert add(-2, -4) == 7