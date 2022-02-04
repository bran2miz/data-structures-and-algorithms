from stacks_and_queue.stack import Stack

class Cat:
    pass

class Dog:
    pass

class AnimalShelter:
	def __init__(self):
		self.in_stack = Stack()
		self.out_stack = Stack()

	def enqueue(self, animal):
		while not self.out_stack.isEmpty():
			self.in_stack.push(self.out_stack.pop())
		self.in_stack.push(animal)

	def dequeue(self, pref = None):
		while not self.in_stack.isEmpty():
			self.out_stack.push(self.in_stack.pop())
		return self.get_pref(pref)

	def get_pref(self, pref):
		if pref == "cat" and isinstance(self.out_stack.peek(), Cat):
			return self.out_stack.pop()
		elif pref == "dog" and isinstance(self.out_stack.peek(), Dog):
			return self.out_stack.pop()
		elif pref == None:
			return self.out_stack.pop()
		elif pref != None and pref != "cat" and pref != "dog":
			return None
		else:
			self.in_stack.push(self.out_stack.pop())
			return self.get_pref(pref)
