"""
Python Data Structures - A Game-Based Approach
Stck class
Emmanuel Owusu - https://linkedin.com/in/codingrev 

"""

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return not self.items

	def push(self, newVal):
		self.items.append(newVal)

	def pop(self):
		return self.items.pop()

	def getStack(self):
		return self.items

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

	def __str__(self):
		return "Stack"

# Class operation test
testStack = Stack()
testStack.push(2)
testStack.push(5)
testStack.push(3)
testStack.pop()
print(testStack.is_empty())
print(testStack.size())
print(testStack.getStack())