# from stacks_and_queue.stack import Stack

# class PseudoQueue:

#     def __init__(self):
#         self.stack_1 = Stack()
#         self.stack_2 = Stack()

#     def enqueue(self, value):
#         while not self.stack_2.isEmpty():
#             self.stack_1.push(self.stack_2.pop())
#         self.stack_1.push(value)

#     def dequeue(self):
#         while not self.stack_1.isEmpty():
#             self.stack_2.push(self.stack_1.pop())
#         return self.stack_2.pop()

from stacks_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        while not self.stack_2.isEmpty():
            self.stack_1.push(self.stack_2.pop())
        self.stack_1.push(value)

    def dequeue(self):
        while not self.stack_1.isEmpty():
            self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()
