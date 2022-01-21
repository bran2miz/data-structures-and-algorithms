from stacks_and_queue.stack import Stack

class AnimalShelter():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    def enqueue(self, animal):
        if animal != 'dog' and animal != 'cat':
            return None
        while self.in_stack.top:
            newValue = self.in_stack.pop()
            self.out_stack.push(newValue)
        self.in_stack.push(animal)
        while self.out_stack.top:
            newValue = self.out_stack.pop()
            self.in_stack.push(newValue)
    def dequeue(self, pref):
        if pref != 'dog' and pref != 'cat':
            return None
        elif pref == 'cat' and self.in_stack.top == 'cat':
            self.in_stack.pop()
        elif pref == 'dog' and self.in_stack.top == 'dog':
            self.in_stack.pop()
