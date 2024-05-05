
def get_Function(word):
	
	get_vowel = 0
	get_consonant = 0
	result = 0
	vowel = ["a", "e", "i", "o", "u"]
	consonant2  = ["b", "c",  "z", "f", "y", "p", "h", "j", "k", "s", "n",  "t", "v", "w", "x", "g",  "m", "d", "q", "r", "t"]
	for index in vowel:
		
		if index in word:
			get_vowel += 1
			
			#else:
	for index in consonant2:

		if index in word:
			get_consonant  += 1
		
	return f"consonant {get_consonant} vowel {get_vowel} "

print(get_Function("consonant"))