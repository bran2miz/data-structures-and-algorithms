from stacks_and_queue.stack import Stack

def validate_brackets(str):
    bracket_stack = Stack()
    dictionary = {'{': '}', '(': ')', '[': ']'}
    for char in str:
        if char in '{[(':
            bracket_stack.push(char)
        elif char in '}])':
            if dictionary[bracket_stack.pop()] != char:
                return False
    if bracket_stack.isEmpty():
        return True
    else:
        return False
