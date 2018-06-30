import random
import string

myString = "This is a test myString for testing purposes. The quick brown fox!! M!!!!!"
ALPH = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def obfuscate(myString):
	splitmyString = myString.split()
	resultantSplit = []
	for word in splitmyString:
		if len([i for i in word if i not in string.punctuation]) <= 3:
			resultantSplit.append(word)
			continue
		firstPart = word[0]
		index = -1
		while not any(char in ALPH for char in word[index:]):
			index -= 1
		lastPart = word[index:]
		middlePart = ''.join(random.sample(word[1:index],len(word[1:index])))
		resultantSplit.append(firstPart+middlePart+lastPart)
	return ' '.join(resultantSplit)



print(obfuscate(myString))
