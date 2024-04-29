from isPalindrome import is_Palindrome


def test_for_palindrome_returns_true():
	assert is_Palindrome('malam') == true
	assert is_Palindrome('12121') == false
	assert is_Palindrome('never odd or even')


def test_for_palindrome_returns_false():
	assert is_Palindrome('ball') == false
	assert is_Palindrome('10111') == false

def test_for_number_return_false():
	assert is_palindrome(10) == false
	assert is_palindrome(10.5) == false
	
	

	
