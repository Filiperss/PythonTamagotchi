def game2(self, choice, chars_missing):
	#words = ["apple", "butter", "cat", "dog", "elephant", "future", "ghost", "history", "icing", "jump", "kill", "little", "moth", "naughty", "octopus", "peanut", "quit", "race", "simple", "terrible", "unbeatable", "very", "wild", "xenoblast", "yoda", "zap"]
	#choice = random.randint(0, len(words) - 1)
	#word = words[choice]
	word = choice
	hidden = '_' * len(word)
	hide = []
	for i in range(3):
		letter = word[int(chars_missing[i])]#word[random.randint(0, len(word) - 1)]
		if(letter not in hide):
			hide.append(letter)
	hidden = self.wordChange(word, hide)
	letters = []
	attempts = 6
	while(attempts > 0):
		guess = input("Make a letter guess! %s You have %d guesses remaining! " % (hidden, attempts))
		if(guess in hide):
			hide.remove(guess)
			hidden = self.wordChange(word, hide)
		else:
			letters.append(guess)
			attempts -= 1
		print("So far you have incorrectly guessed")
		print(letters)
		if(not hide):
			print("Great job! %s" % (word))
			return True

	print("You failed! And should be ashamed... %s " % (word))
	return False