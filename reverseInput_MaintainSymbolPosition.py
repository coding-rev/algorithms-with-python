"""
Objective

Write a python script that reverse a user's input
but keeps any symbol at it's original position after
the reverse

Emmanuel Owusu(Backend Engineer @mPedigree) - https://linkedin.com/in/codingrev
"""

# Code

userInput = input("Enter a word : ")

def conCatElements(Array):
	word = ''
	for element in Array:
		word+=element 
	return word

def reverseAlphaAndMaintainSymbolFunction():
	symbolAndPosition = {}
	filteredWord = []
	symbols = "`~!@#$%^&*()_+=-/><']{"

	# Filtering symbol from word
	for userInputCount in range(0,len(userInput)):
		if userInput[userInputCount] in symbols:
			symbolAndPosition[userInputCount]=userInput[userInputCount]
			
		else:
			filteredWord.append(userInput[userInputCount])

	# Reversing filtered Word
	filteredWord = filteredWord[::-1]

	# Adding symbols back to their original position
	for symbolIndex, symbolValue in symbolAndPosition.items():
		filteredWord.insert(symbolIndex, symbolValue)

	return conCatElements(filteredWord)


result = reverseAlphaAndMaintainSymbolFunction()
print("Result : ", result)