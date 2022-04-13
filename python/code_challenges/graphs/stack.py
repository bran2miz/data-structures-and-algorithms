class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'a Node with a value of {self.value}'

    def __repr__(self):
        return f'Node(value: {self.value}, next: {self.next})'

class Stack:
    def __init__(self, top = None):
        self.top = top

    def __str__(self):
        return f'A Stack, its top holds {self.top}'

    def __repr__(self):
        return f'Stack(top: Node({self.front}))'

    def push(self, value):
        '''
        Adds a new node with input value to the top of the stack with an O(1) Time performance.
        input: value as any value
        output: None
        '''
        node = Node(value)

        if self.top == None:
            self.top = node
        else:
            temp_top = node
            temp_top.next = self.top
            self.top = temp_top

    def pop(self):
        '''
        Returns the value of the node from the top of the stack. Removes the node from the top of the stack. Should raise exception when called on empty stack
        input: None
        output: value of Node from top of stack
        '''
        if self.top == None:
            raise Exception('Stack is empty.')
        ret_node = self.top
        self.top = self.top.next

        return ret_node.value

    def peek(self):
        '''
        Returns the value of the node located at the top of the stack. Should raise exception when called on empty stack.
        input: None
        output: Value of top node of stack
        '''

        if self.top == None:
            raise Exception('Stack is empty.')
        else:
            return self.top.value

    def is_empty(self):
        '''
        Returns a boolean indicating whether or not the stack is empty
        input: None
        output: Boolean
        '''
        if self.top:
            return False
        else:
            return True
